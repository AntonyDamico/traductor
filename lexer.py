import ply.lex as lex
import sys
import re

# Palabras Reservadas
reserved = (
    'var',
    'function',
    'write',
    'while',
    'if',
    'for',
    'return',
    'else'
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
    'COMMA',
    'STRINGS',
    'EQUALS',
    'LT',
    'GT',
    'LE',
    'GE',
    'NE',
    'AND',
    'OR',
    'NOT',
    'INCREMENT',
    'DECREMENT',
    'TRUE',
    'FALSE',
    'PROMPT'
) + tuple(map(lambda s: s.upper(), reserved))


# Arithmetic Operators
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MOD = r'\%'
t_INCREMENT = r'\+\+'
t_DECREMENT = r'--'

# Relational Operators
t_GE = r'>='
t_LE = r'<='
t_EQUALS = r'=='
t_NE = r'!='
t_LT = r'<'
t_GT = r'>'

# Logic Operators
t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'\!'
t_TRUE = r'true'
t_FALSE = r'false'

t_END_LINE = r';'
t_ASSIGN = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\{'
t_RBRACKET = r'\}'
t_COMMA = r','

# Strings
# t_STRINGS = r'\"([^\\\n]|(\\(.|\n)))*?\"'
t_STRINGS = r'(?:\'|\").*(?:\'|\")'
# Ignoring spaces and tabs
t_ignore = ' \t\v'
# Ignoring multiline comments
t_ignore_COMMENT = r'/\*(.|\n)*?\*/'


def t_NUMBER(t):
    r'\d+\.?(\d+)?'
    if eval(t.value) <= 32767 and '.' not in t.value:
        t.value = eval(t.value)
        return t
    else:
        print("Lexical: illegal character '%s' in line '%d' position" %
              (t.value, t.lineno))
        t.lexer.skip(1)


def t_ID(t):
    r'[a-zA-z_]\w*'
    if t.value in reserved:
        t.type = t.value.upper()
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_comment(t):
    r'\//.*'
    pass


def t_error(t):
    print("Lexical: illegal character '%s' in line '%d' position" %
          (t.value[0], t.lineno))
    t.lexer.skip(1)


lex.lex(reflags=re.UNICODE)

# MAIN
if __name__ == "__main__":
    f = open(sys.argv[1], 'r')
    datos = f.read()
    f.close()
    lex.input(datos)

    while 1:
        token = lex.token()
        if not token:
            break
        print(token)
