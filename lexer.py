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

		# main and end main
		self.lexer.add('START_MAIN', r'(main)')
		self.lexer.add('END_MAIN', r'(end main)')
		self.lexer.add('END', r'end')

		# Prompt
		self.lexer.add('PROMPT', r'(prompt)')

		# For and End for
		self.lexer.add('FOR', r'(for)')
		self.lexer.add('END_FOR', r'(end for)')

		# While and End While
		self.lexer.add('WHILE', r'(while)')
		self.lexer.add('END_WHILE', r'(end while)')

		# If and End If
		self.lexer.add('IF', r'(if)')
		self.lexer.add('THEN', r'(then)')
		self.lexer.add('END_IF', r'(end if)')

		# Else
		self.lexer.add('ELSE', r'(else)')

		# Let
		self.lexer.add('LET', r'(let)')

		#Call
		self.lexer.add('CALL', r'(call)')

		# Code Struture Operators
		######################################

		# Parenthesis
		self.lexer.add('OPEN_PAREN', r'\(')
		self.lexer.add('CLOSE_PAREN', r'\)')

		# Comma
		self.lexer.add('COMMA', r'\,')

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

		# Relation Operators
		######################################
	
		self.lexer.add('EQUAL', r'(=)')
		self.lexer.add('DIFF', r'(<>)')
		self.lexer.add('GTE', r'(>=)')
		self.lexer.add('LTE', r'(<=)')
		self.lexer.add('GREATER', r'(>)')
		self.lexer.add('LESS', r'(<)')

		# Assign
		self.lexer.add('ASSIGN', r'(::=)')
		
		# Data Types
		######################################

		# Number
		self.lexer.add("NUMBER", r"\d+")

		# Variables
		######################################

		# Var Declaration
		self.lexer.add('VAR_DECL', r'define')

		# Var Type
		self.lexer.add('VAR_TYPE', r'integer')

		# Var ID
		self.lexer.add("VAR_ID", r"[a-zA-Z0-9]+")


		# Other Stuff
		######################################

		# Function Declaration
		self.lexer.add('FUNC_DECL', r'(function)')

		# Ignore spaces
		self.lexer.ignore(r"\s+")

	def get_lexer(self):
		self._add_tokens()
		return self.lexer.build()

