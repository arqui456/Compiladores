from lexer import Lexer
from parser import Parser
import copy

text_input = """
print(3 + 2)
end_main
print(3 * 2)
end_main
print(5 = 5)
end_main
print(3 > 6)
end_main
define x ::= 20
end_main
"""

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)
token_list = copy.copy(tokens)

for token in token_list:
	print(token)

print("\nINPUT:", text_input)
print("OUTPUT:")

pg = Parser()
pg.parse()
parser = pg.get_parser(tokens)
parser.parse(tokens).eval()



