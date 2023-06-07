import os
from lexico import LexicalAnalyzer
from sintatico import Parser

current_directory = os.getcwd()

file_name = "codigo.txt"

file_path = os.path.join(current_directory, file_name)

with open(file_path, "r") as file:
    source_code = file.read()

tokens = LexicalAnalyzer(source_code)
parser = Parser(tokens)
print(parser.parse())


