from core.parser.script_parser import Parse
from core.parser.script_lexer import Lexer


def interpreter(target):
    """1. Json parse 2. convert it to python code"""
    tokenize = Lexer(target).lexer()
    for i in range(len(tokenize)):
        print(tokenize[i])

    scr = Parse(tokenize)
