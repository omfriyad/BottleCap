from rply import ParserGenerator
from ast import *
from lexer import operators


class Parser():
    def __init__(self):
        # The list of tokens from the lexer file
        self.pg = ParserGenerator(
            [token for token in operators.keys()],
            precedence=[
                ("left", ["ADD", "SUBTRACT"]),
                ("left", ["MULTIPLY", "DIVIDE"]),
            ]
        )

    def parse(self):

        @self.pg.production('program : expression')
        def program(p):
            return Program(p[0])

        @self.pg.production('expression : expression expression')
        def expression(p):
            return Expression(p)

        @self.pg.production('expression : PRINT expression')
        def print_(p):
            return Print(p[1])

        # Binary operations

        @self.pg.production('expression : ADD expression WITH expression')
        def add(p):
            return Add(p[1], p[3])

        @self.pg.production('expression : SUBTRACT expression FROM expression')
        def subtract(p):
            return Subtract(p[1], p[3])

        @self.pg.production('expression : MULTIPLY expression BY expression')
        def multiply(p):
            return Multiply(p[1], p[3])

        @self.pg.production('expression : DIVIDE expression BY expression')
        def divide(p):
            return Divide(p[1], p[3])

        # Handle assinging
        @self.pg.production('expression : ASSIGN variable_name TO expression')
        def assign(p):
            return Assign(p[1], p[3])

        # defining expressions
        @self.pg.production('expression : variable_name')
        @self.pg.production('variable_name : IDENTIFIER')
        def identifier(p):
            return Identifier(p[0].value)

        @self.pg.production('expression : NUMBER')
        def number(p):
            return Number(p[0].value)

        @self.pg.production('expression : STRING')
        def string(p):
            return String(p[0].value)

        @self.pg.production('expression : RPN')
        def rpn(p):
            return Rpn(p[0].value)

        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()

