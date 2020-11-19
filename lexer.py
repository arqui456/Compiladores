#from generator import LexerGenerator
from rply import LexerGenerator

class Lexer():
	def __init__(self):
		self.lexer = LexerGenerator()

	def _add_tokens(self):

		# Core language functions
		######################################

		# Print
		self.lexer.add('PRINT', r'print')

		# Code Struture Operators
		######################################

		# Parenthesis
		self.lexer.add('OPEN_PAREN', r'\(')
		self.lexer.add('CLOSE_PAREN', r'\)')

		# Semi Colon
		self.lexer.add('SEMI_COLON', r'\;')

		# Math Operators
		######################################

		# Sum
		self.lexer.add('SUM', r'\+')

		# Subtration
		self.lexer.add('SUB', r'\-')

		# Multiplication
		self.lexer.add('MULT', r'\*')

		# Exponential
		self.lexer.add('EXP', r'\^')

		# Division
		self.lexer.add('DIV', r'\/')

		# Modulus
		self.lexer.add('MOD', r'\%')
		
		# Data Types
		######################################

		# Number
		self.lexer.add("NUMBER", r"\d+")

		# Other Stuff
		######################################

		# Ignore spaces
		self.lexer.ignore(r"\s+")

	def get_lexer(self):
		self._add_tokens()
		return self.lexer.build()

