import functools

def CustomCoroutineWrapper(func):
	"Initialzie automatically."
	@functools.wraps(func)
	def init(*args, **kwargs):
		cr_obj = func(*args, **kwargs)
		next(cr_obj)
		return cr_obj
	return init

class GCodeElementBase:
	"G-code element"
	element = None
	def __init__(self, element = None):
		self.element = element
	def __str__(self):
		return self.element

class GCodePrefix(GCodeElementBase):
	"G-code prefix"
	def __repr__(self):
		return 'GCodePrefix: {}'.format(self.element)

class GCodeFloat(GCodeElementBase):
	"G-code float"
	def __repr__(self):
		return 'GCodeFloat: {}'.format(self.element)

class GCodeElementHandler:
	"Handler of G-code elements"
	memebr_tuple = None
	def __init__(self, builtin_element_tuple):
		temporary_list = list()
		for x in builtin_element_tuple:
			if type(x) == type(str()):
				temporary_list.append(GCodePrefix(x))
			elif type(x) == type(float()):
				temporary_list.append(GCodeFloat(x))
			elif type(x) == type(GCodePrefix()) or type(GCodeFloat()):
				temporary_list.append(x)
		self.memebr_tuple = tuple(temporary_list)
	def __repr__(self):
		return 'GCodeElementHandler: {}'.format(self.memebr_tuple)


class GCodeBase:
	"Basic G-code object"
	prefix = GCodePrefix('')
	number = GCodeFloat(0)
	def __init__(self, number):
		self.number = number
	def __str__(self):
		return '{}{}'.format(str(self.prefix), str(self.number))
	def __repr__(self):
		return 'GCode: {}{}'.format(str(self.prefix), str(self.number))

class GCodeG(GCodeBase):
	"Address for preparatory commands"
	prefix = GCodePrefix('G')

class GCodeX(GCodeBase):
	"Absolute or incremental position of X axis"
	prefix = GCodePrefix('X')

class GCodeY(GCodeBase):
	"Absolute or incremental position of Y axis"
	prefix = GCodePrefix('Y')

class GCodeException(Exception):
	"Basic exception class for G-code handling"
	pass

class GCodeSyntaxError(GCodeException):
	"G-code Syntax Error"
	pass