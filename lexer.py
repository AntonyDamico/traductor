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
    'NOTCLA',
    'QUOTE'
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
        print ("Lexical: illegal character '%s' in line '%d' position" % (t.value, t.lineno))
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
    print ("Lexical: illegal character '%s' in line '%d' position" % (t.value[0], t.lineno))
    t.lexer.skip(1)


lex.lex()

# MAIN 
if __name__ == "__main__":
    f = open(sys.argv[1],'r')
    datos = f.read()
    f.close()
    lex.input(datos)
    
    while 1 :
    	token = lex.token()
    	if not token: break
    	print(token)