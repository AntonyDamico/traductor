from lexer import tokens
import ply.yacc as yacc
import sys

precedence = (
    ('left', 'ORLOGIC'),
    ('left', 'ANDLOGIC'),
    ('left', 'ASSIGN', 'NOASSIG'),
    ('left', 'GREATERTHAN', 'LESSTHAN', 'LESS', 'GREATER'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE', 'MOD'),
    ('right', 'NOT'),
)

# statements: declarations


def p_rec_statement(p):
    '''S : statement S
         | statement END_LINE S'''
    if len(p) == 3:
        p[0] = ('statement', p[1], p[2])
    else:
        p[0] = ('statement', p[1], p[3])


def p_statement(p):
    'S : statement'
    p[0] = p[1]


def p_declarations(p):
    'statement : declarations'
    p[0] = p[1]


# declarations

def p_variables(p):
    'declarations : VAR ids'
    p[0] = ('VAR', p[2])


def p_write(p):
    'declarations : WRITE LPAREN expressions RPAREN'
    p[0] = ('WRITE', p[3])

def p_if(p):
    'declaration : IF LPAREN condition RPAREN return_dec'
    p[0] = ('IF', p[3], p[5])