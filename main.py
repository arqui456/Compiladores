from lexer import Lexer
from parser import Parser
import copy

text_input = """
main
print(2 + 3) end
if (5 > 3) then print("testando") enif end
if (6 > 3) then print("teste 2") enif end
while (3 > 2) then print(1+1) enile end
end_main
"""

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)
token_list = copy.copy(tokens)

"""
for token in token_list:
	print(token)

print("\nINPUT:", text_input)
print("OUTPUT:")
"""

pg = Parser()
pg.parse()
parser = pg.get_parser(tokens)
parser.parse(tokens).eval()



