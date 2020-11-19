#from generator import ParserGenerator
from rply import ParserGenerator
from ast import *

class Parser():
	def __init__(self):
		self.pg = ParserGenerator(
			# A list of all token names, accepted by the parser.
			['NUMBER', 'PRINT', 'OPEN_PAREN', 'CLOSE_PAREN',
			 'SEMI_COLON', 'SUM', 'SUB', 'MULT', 'DIV', 'EXP', 'MOD'],
			 # A list of precedence rules with ascending precedence, to
			 # disambiguate ambiguous production rules.
			 precedence=[
			 	('left', ['SUM', 'SUB']),
			 	('left', ['MULT', 'DIV', 'MOD']),
			 	('left', ['EXP'])
			 ],
			 cache_id='myparser'
		)

	def parse(self):
		@self.pg.production('program : PRINT OPEN_PAREN expression CLOSE_PAREN SEMI_COLON')
		def program(p):
			return Print(p[2])

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
			raise ValueError(token)

	def get_parser(self):
		return self.pg.build()