class LogicError(Exception):

	message = 'Shouldn''t be possible'

	def __str__(self):
		return self.message

class UnexpectedEndError(Exception):

	message = 'Unexpected end of statement'

	def __str__(self):
		return message

class UnexpectedTokenError(Exception):

	def __init__(self, token):
		self.token = token

	def __str__(self):
		return self.token

class ImmutableError(Exception):

	message = 'Cannot assign to imutable variable %s'

	def __init__(self, name):
		self.name = name

	def __str__(self):
		return self.message % self.name