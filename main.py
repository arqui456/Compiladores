from lexer import Lexer
from parser import Parser

text_input = """
print(4 * 2 + 4 * 2);
"""

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)

print("INPUT:", text_input)
print("OUTPUT:")

"""
for token in tokens:
	print(token)
"""

pg = Parser()
pg.parse()
parser = pg.get_parser()
parser.parse(tokens).eval()

