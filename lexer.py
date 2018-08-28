from collections import OrderedDict
from rply import LexerGenerator, Token

operators = OrderedDict([
    ("PRINT",r"Print"),
    ("ADD",r"Add"),
    ("SUBTRACT",r"Subtract"),
    ("MULTIPLY",r"Multiply"),
    ("DIVIDE",r"Divide"),
    ("ASSIGN",r"Assign"),
    ("WITH",r"with"),
    ("FROM",r"from"),
    ("BY",r"by"),
    ("TO",r"to"),
    ("RPN",r"[0-9][0-9\' '\+\-\/\*]+"),     # [0-9\' '\+\-\/\*]*
    ("NUMBER",r"[0-9]+"),
    ("STRING",r"\"[A-Za-z0-9_]+[A-Za-z0-9_\' ']+\""),
    ("IDENTIFIER", r"[A-Za-z][A-Za-z0-9_]+")
])


class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        for key, value in operators.items():
            self.lexer.add(key, value)
        self.lexer.ignore(r'\s+')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()




