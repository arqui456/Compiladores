#from generator import ParserGenerator
from rply import ParserGenerator
from ast import *
from errors import *
import lexer

class Parser():
	def __init__(self):
		# We want to hold a dict of declared variables
		self.variables = {}
		# A list of all token names, accepted by the parser.
		self.pg = ParserGenerator(
			['NUMBER', 'PRINT', 'OPEN_PAREN', 'CLOSE_PAREN',
			 'END', 'SUM', 'SUB', 'MULT', 'DIV', 'EXP', 'MOD',
			 'START_MAIN', 'END_MAIN', 'EQUAL', 'DIFF', 'GTE',
			 'GREATER', 'LESS','LTE'],
			 # A list of precedence rules with ascending precedence, to
			 # disambiguate ambiguous production rules.
			 precedence=[
			 	('left', ['EQUAL', 'DIFF', 'GTE', 'GREATER', 'LESS', 'LTE']),
			 	('left', ['SUM', 'SUB']),
			 	('left', ['MULT', 'DIV', 'MOD']),
			 	('left', ['EXP'])
			 ],
			 cache_id='myparser'
		)


	def parse(self):

		@self.pg.production('program : PRINT OPEN_PAREN expression CLOSE_PAREN END')
		def program(p):
			return Print(p[2])

		@self.pg.production('expression : expression EQUAL expression')
		@self.pg.production('expression : expression DIFF expression')
		@self.pg.production('expression : expression GTE expression')
		@self.pg.production('expression : expression LTE expression')
		@self.pg.production('expression : expression GREATER expression')
		@self.pg.production('expression : expression LESS expression')
		def expression_equality(p):
			left = p[0]
			right = p[2]
			check = p[1]
			if check.gettokentype() == 'EQUAL':
				return Equal(left, right)
			elif check.gettokentype() == 'DIFF':
				return NotEqual(left, right)
			elif check.gettokentype() == 'GTE':
				return GreaterThanEqual(left, right)
			elif check.gettokentype() == 'LTE':
				return LessThanEqual(left, right)
			elif check.gettokentype() == 'GREATER':
				return GreaterThan(left, right)
			elif check.gettokentype() == 'LESS':
				return LessThan(left, right)
			else:
				raise LogicError()

		@self.pg.production('expression : expression SUM expression')
		@self.pg.production('expression : expression SUB expression')
		@self.pg.production('expression : expression MULT expression')
		@self.pg.production('expression : expression DIV expression')
		@self.pg.production('expression : expression EXP expression')
		@self.pg.production('expression : expression MOD expression')
		def expression(p):
			left = p[0]
			right = p[2]
			operator = p[1]
			if operator.gettokentype() == 'DIV':
				return Div(left, right)
			elif operator.gettokentype() == 'MULT':
				return Mult(left, right)
			elif operator.gettokentype() == 'SUM':
				return Sum(left, right)
			elif operator.gettokentype() == 'SUB':
				return Sub(left, right)
			elif operator.gettokentype() == 'EXP':
				return Exp(left, right)
			elif operator.gettokentype() == 'MOD':
				return Mod(left, right)
			else:
				raise AssertionError('Oops, this should not be possible!')
			
		@self.pg.production('expression : NUMBER')
		def number(p):
			return Number(p[0].value)

		@self.pg.error
		def error_handle(token):
			# We print our state for debugging purporses
			print(token)
			pos = token.getsourcepos()
			if pos:
				raise UnexpectedTokenError(token.gettokentype())
			elif token.gettokentype() == '$end':
				raise UnexpectedEndError()
			raise ValueError(token)		

	def get_parser(self, tokens):
		return self.pg.build()
		