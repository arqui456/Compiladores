from errors import *

class Program():

	def __init__(self, statement):
		self.statements = []
		self.statements.append(statement)

	def add_statement(self, statement):
		self.statements.insert(0, statement)

	def eval(self):
		result = None
		for statement in self.statements:
			result = statement.eval()
		return result

	def get_statements(self):
		return self.statements

class Block():

	def __init__(self, statement):
		self.statements = []
		self.statements.append(statement)

	def add_statement(self, statement):
		self.statements.append(0, statement)

	def get_statements(self):
		return self.statements

	def eval(self):
		result = None
		for statement in self.statements:
			result = statement.eval()
		return result

class FunctionDeclaration():

	def __init__(self, name, args, block):
		self.name = name
		self.args = args
		self.block = block

	def eval(self):
		raise LogicError("Cannot assign to this")

	def to_string(self):
		return "<function '%s'>" % self.name

class Call():

	def __init__(self, name, args):
		self.name = name
		self.args = args

	def eval(self):
		result = Null()
		return result

	def to_string(self):
		return "<call %s'>" % self.name

class Null():

	def eval(self):
		return self

	def to_string(self):
		return 'null'

	def rep(self):
		return 'Null()'

class Array():

	def map(self, fun, ls):
		nls = []
		for l in ls:
			nls.append(fun(l))
		return nls

	def __init__(self, inner):
		self.statements = inner.get_statements()
		self.values = []

	def get_statements(self):
		return self.statements

	def push(self, statement):
		self.statements.insert(0, statement)

	def append(self, statement):
		self.statements.append(statement)

	def index(self, i):
		if type(i) is Integer:
			return self.values[i.value]
		if type(i) is Float:
			return self.values[int(i.value)]
		raise LogicError("Cannot index with that value")

	def add():
		if type(right) is Array:
			result = Array(InnerArray())
			result.values.extend(self.values)
			result.values.extend(right.values)
			return result
		raise LogicError("Cannot add that to array")

	def eval(self):

		if len(self.values) == 0:
			for statement in self.statements:
				self.values.append(statement.eval())
		return self

	def to_string():
		return '[%s]' % (", ".join(self.map(lambda x: x.to_string(), self.values)))

class InnerArray():

	def __init__(self, statements = None):
		self.data = {}
		self.values = {}
		if statements:
			self.data = statements

	def update(self, key, val):
		self.data[key] = val

	def get_data(self):
		return self.data

class Variable():

	def __init__(self, name):
		self.name = str(name)
		self.value = None

	def getname(self):
		return str(self.name)

	def eval(self, variables):
		if variables.get(self.name, None) is not None:
			self.value = variables[self.name].eval()
			return self.value
		return LogicError("Not yet defined")

	def to_string(self):
		return str(self.name)


class Number():
	"""docstring for Number"""
	def __init__(self, value):
		self.value = value

	def eval(self):
		return int(self.value)

class Integer():

	def __init__(self, value):
		self.value = value

	def eval(self):
		return self.value

	def to_string(self):
		return str(self.value)

class Float():

	def __init__(self, value):
		self.value = value

	def eval(self):
		return self

	def to_string(self):
		return str(self.value)

class String():

	def __init__(self, value):
		self.value = value

	def eval(self):
		return self.value

	def to_string(self):
		return '"%s"' % str(self.value)

class Boolean():
	def __init__(self, value):
		self.value = bool(value)

	def eval(self):
		return self

class Not():

	def __init__(self, value):
		self.value = value

	def eval(self):
		result = self.value.eval()
		if isinstance(result, Boolean):
			return Boolean(not result.value)
		raise LogicError("Cannot 'not' that")

class BinaryOp():
	"""docstring for BinaryOp"""
	def __init__(self, left, right):
		self.left = left
		self.right = right

class Sum(BinaryOp):
	"""docstring for Sum"""
	def eval(self):
		return self.left.eval() + self.right.eval()

class Sub(BinaryOp):
	"""docstring for Sum"""
	def eval(self):
		return self.left.eval() - self.right.eval()

class Mult(BinaryOp):
	"""docstring for Mult"""
	def eval(self):
		return self.left.eval() * self.right.eval()

class Div(BinaryOp):
	"""docstring for Div"""
	def eval(self):
		return self.left.eval() // self.right.eval()

class Exp(BinaryOp):
	"""docstring for Exp"""
	def eval(self):
		return self.left.eval() ** self.right.eval()

class Mod(BinaryOp):
	"""docstring for Mod"""
	def eval(self):
		return self.left.eval() % self.right.eval()

class Index(BinaryOp):

	def eval(self):
		left = self.left.eval()
		if type(left) is Array:
			return left.index(self.right.eval())
		if type(left) is String:
			return left.index(self.right.eval())

		raise LogicError("Cannot index this")


class If():

	def __init__(self, condition, body, else_body=Null()):
		self.condition = condition
		self.body = body
		self.else_body = else_body

	def eval(self):
		condition = self.condition.eval()
		if Boolean(True).value == condition:
			return self.body.eval()
		elif type(self.else_body) is not Null:
			return self.else_body.eval()
		return Null()

class While():

	def __init__(self, condition, body):
		self.condition = condition
		self.body = body

	def eval(self):
		while Boolean(True).value == self.condition.eval():
			return self.body.eval()
		return Null()

### Logic ###
class Equal(BinaryOp):
	"""docstring for Equal"""
	def eval(self):
		return self.left.eval() == self.right.eval()

class NotEqual(BinaryOp):
	"""docstring for NotEqual"""
	def eval(self):
		return self.left.eval() != self.right.eval()

class GreaterThan(BinaryOp):
	"""docstring for GreaterThan"""
	def eval(self):
		return self.left.eval() > self.right.eval()

class LessThan(BinaryOp):
	"""docstring for LessThat"""
	def eval(self):
		return self.left.eval() < self.right.eval()

class GreaterThanEqual(BinaryOp):
	"""docstring for GreaterThanEqual"""
	def eval(self):
		return self.left.eval() >= self.right.eval()
		
class LessThanEqual(BinaryOp):
	"""docstring for LessThatEqual"""
	def eval(self):
		return self.left.eval() <= self.right.eval()

class Print():
	"""docstring for Print"""
	def __init__(self, value):
		self.value = value

	def eval(self):
		print(self.value.eval())

class Assignment(BinaryOp, Variable):

	def eval(self, variables):
		if isinstance(self.left, Variable):
			if variables.get(self.left.getname(), None) is None:
				variables[self.left.getname()] = self.right
				return self.right.eval()
			raise ImmutableError(self.left.getname())
		raise LogicError()
		
		
		