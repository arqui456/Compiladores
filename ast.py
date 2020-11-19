
class Number():
	"""docstring for Number"""
	def __init__(self, value):
		self.value = value

	def eval(self):
		return int(self.value)

class BinaryOp():
	"""docstring for BinaryOp"""
	def __init__(self, left, right):
		self.left = left
		self.right = right

class Sum(BinaryOp):
	"""docstring for Sum"""
	def eval(self):
		return self.left.eval() + self.right.eval()

class Print():
	"""docstring for Print"""
	def __init__(self, value):
		self.value = value

	def eval(self):
		print(self.value.eval())
		
		
		