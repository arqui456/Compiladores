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
			 'GREATER', 'LESS','LTE', 'NEWLINE', 'VAR_DECL',
			 'VAR_TYPE', 'VAR_ID', 'ASSIGN', 'FUNC_DECL',
			 'STRING', 'COMMA', 'NOT', 'OPEN_BRACKET',
			 'CLOSE_BRACKET', 'IF', 'ELSE', 'WHILE', 'THEN'],
			 # A list of precedence rules with ascending precedence, to
			 # disambiguate ambiguous production rules.
			 precedence=[
			 	('left', ['VAR_DECL','PRINT']),
			 	('left', ['ASSIGN']),
			 	('left', ['OPEN_BRACKET', 'CLOSE_BRACKET', 'COMMA']),
			 	('left', ['IF', 'THEN', 'ELSE', 'END', 'NEWLINE', 'WHILE']),
			 	('left', ['NOT']),
			 	('left', ['EQUAL', 'DIFF', 'GTE', 'GREATER', 'LESS', 'LTE']),
			 	('left', ['SUM', 'SUB']),
			 	('left', ['MULT', 'DIV', 'MOD']),
			 	('left', ['EXP'])
			 ],
			 cache_id='myparser'
		)


	def parse(self):

		variables = self.variables

		@self.pg.production('main : START_MAIN program')
		@self.pg.production('main : program')
		def main_program(p):
			return p[0]

		@self.pg.production('program : statement_full')
		def program_statement(p):
			return Program(p[0])

		@self.pg.production('program : statement_full program')
		def program_statement_program(p):
			if type(p[1]) is Program:
				program = p[1]
			else:
				program = Program(p[1])
			program.add_statement(p[0])
			return p[1]

		@self.pg.production('block : statement_full')
		def block_expr(p):
			return Block(p[0])

		@self.pg.production('block : statement_full block')
		def block_expr_block(p):
			if type(p[1]) is Block:
				block = p[1]
			else:
				block = Block(p[1])
			block.add_statement(p[0])
			return b

		@self.pg.production('statement_full : statement NEWLINE')
		@self.pg.production('statement_full : statement END_MAIN')
		def statement_full(p):
			return p[0]

		@self.pg.production('statement : expression')
		def statement_expr(p):
			return p[0]

		@self.pg.production('statement : VAR_DECL VAR_ID ASSIGN expression')
		def statement_assignment(p):
			return Assignment(Variable(p[1].getstr()), p[3])

		@self.pg.production('statement : FUNC_DECL VAR_ID OPEN_PAREN arglist CLOSE_PAREN VAR_TYPE NEWLINE block END')
		def statement_func(p):
			return FunctionDeclaration(p[1].getstr(), Array(p[3]), p[7])

		@self.pg.production('statement : FUNC_DECL VAR_ID OPEN_PAREN CLOSE_PAREN VAR_TYPE NEWLINE block END')
		def statement_func_noargs(p):
			return FunctionDeclaration(p[1].getstr(), Null(), p[6])

		@self.pg.production('expression : NUMBER')
		def expression_number(p):
			return Integer(int(p[0].getstr()))

		@self.pg.production('expression : STRING')
		def expression_string(p):
			return String(p[0].getstr().strip('"\''))

		@self.pg.production('expression : OPEN_BRACKET expression CLOSE_BRACKET')
		def expression_array_single(p):
			return Array(InnerArray([p[1]]))

		@self.pg.production('expression : OPEN_BRACKET expressionlist CLOSE_BRACKET')
		def expression_array(p):
			return Array(p[1])

		@self.pg.production('expressionlist : expression')
		@self.pg.production('expressionlist : expression COMMA')
		def expressionlist_single(p):
			return InnerArray([p[0]])

		@self.pg.production('expressionlist : expression COMMA expressionlist')
		def arglist(p):
			# expressionList should already be an InnerArray
			p[2].push(p[0])
			return p[2]

		@self.pg.production('arglist : VAR_ID')
		@self.pg.production('arglist : VAR_ID COMMA')
		def arglist_single(p):
			return InnerArray([Variable(p[0].getstr())])

		@self.pg.production('expression : expression OPEN_BRACKET expression CLOSE_BRACKET')
		def expression_array_index(p):
			return Index(p[0], p[2])

		@self.pg.production('expression : IF expression THEN statement END')
		def expression_if_single_line(p):
			return If(condition=p[1], body=p[3])

		@self.pg.production('expression : IF expression THEN statement ELSE THEN statement END')
		def expression_if_else_single_line(p):
			return If(condition=p[1], body=p[3], else_body=p[6])

		@self.pg.production('expression : IF expression THEN NEWLINE block END')
		def expression_if(p):
			return If(condition=p[1], body=p[4])

		@self.pg.production('expression : IF expression THEN NEWLINE block ELSE THEN NEWLINE block END')
		def expression_if_else(p):
			return If(condition=p[1], body=p[4], else_body=p[8])

		@self.pg.production('expression : WHILE expression THEN NEWLINE block END')
		def expression_while(p):
			return While(condition=p[1], body=p[4])

		@self.pg.production('expression : VAR_ID')
		def expression_variable(p):
			# cannot return the value of a variable if it isn't yet defined
			return Variable(p[0].getstr())

		@self.pg.production('expression : VAR_ID OPEN_PAREN CLOSE_PAREN')
		def expression_call_noargs(p):
			return Call(p[0].getstr(), InnerArray())

		@self.pg.production('expression : VAR_ID OPEN_PAREN expressionlist CLOSE_PAREN')
		def expression_call_args(p):
			# cannot return the value of a variable if it isn't yet defined
			return Call(p[0].getstr(), p[2])

		@self.pg.production('expression : NOT expression')
		def expression_not(p):
			return Not(p[1])

		@self.pg.production('expression : OPEN_PAREN expression CLOSE_PAREN')
		def expression_parens(p):
			# in this case we need parens only for precedence
			# so we just need to return the inner expression
			return p[1]
		
		"""
		@self.pg.production('program : PRINT OPEN_PAREN expression CLOSE_PAREN END')
		def program(p):
			return Print(p[2])
		"""
		@self.pg.production('expression : PRINT OPEN_PAREN expression CLOSE_PAREN')
		def print_func(p):
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
			elif token.gettokentype() == 'END_MAIN':
				raise UnexpectedEndError()
			raise ValueError(token)		

	def get_parser(self, tokens):
		return self.pg.build()
		