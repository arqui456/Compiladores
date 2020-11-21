from lexer import Lexer
from parser import Parser
import copy

text_input = """
print(4 ^ 2);
"""
print("\nINPUT:", text_input)

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)
tokens_list = copy.copy(tokens)

for token in tokens_list:
    print(token)

print("\nINPUT:", text_input)
print("OUTPUT:")

pg = Parser()
pg.parse()
parser = pg.get_parser()
parser.parse(tokens).eval()
