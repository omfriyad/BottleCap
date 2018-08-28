from lexer import Lexer
from parser import Parser

text_input = """
 Print Add 5 with Print Add 3 with Multiply 2 5 * by Assign var to 3

"""

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)

pg = Parser()
pg.parse()
parser = pg.get_parser()
parser.parse(tokens).eval()