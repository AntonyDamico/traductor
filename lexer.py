import ply.lex as lex
import sys

# Palabras Reservadas
reserved = (
    'var',
    'function',
    'write',
    'prompt',
    'if',
    'for',
    'while',
    'return'
)

# Lista de tokens mas las palabras reservadas
# en la forma (RESERVADA: reservada)
tokens = (
    'END_LINE',
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'MOD',
    'ASSIGN',
    'LPAREN',
    'RPAREN',
    'LBRACKET',
    'RBRACKET',
    'ID',
    'COMA',
    'STRINGS',
    'EQUALS',
    'LESS',
    'GREATER',
    'LESSTHAN',
    'GREATERTHAN',
    'NOTASSIG',
    'ANLOGIC',
    'ORLOGIC',
    'NOTCLA'
) + tuple(map(lambda s: s.upper(), reserved))


# Arithmetic Operators
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MOD = r'\%'

# Relational Operators
t_GREATERTHAN = r'>='
t_LESSTHAN = r'<='
t_EQUALS = r'=='
t_NOTASSIG = r'!='
t_LESS = r'<'
t_GREATER = r'>'

# Logic Operators
t_ANLOGIC = r'&&'
t_ORLOGIC = r'\|\|'
t_NOTCLA = r'\!'

t_END_LINE = r';'
t_ASSIGN = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\{'
t_RBRACKET = r'\}'
t_COMA = r','

# Strings
t_STRINGS = r'\"([^\\\n]|(\\(.|\n)))*?\"'
# Ignoring spaces and tabs
t_ignore = ' \t\v'
# Ignoring multiline comments
t_ignore_COMMENT = r'/\*(.|\n)*?\*/'
