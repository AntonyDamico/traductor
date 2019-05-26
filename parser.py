from lexer import tokens
import ply.yacc as yacc
import sys

precedence = (
    ('left', 'ORLOGIC'),
    ('left', 'ANDLOGIC'),
    ('left', 'ASSIGN', 'NE'),
    ('left', 'GE', 'LE', 'LT', 'GT'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE', 'MOD'),
    ('right', 'NOT'),
)


# =================================
# ||        Statements           ||
# =================================

def p_rec_statement(p):
    '''S : statement S
         | statement END_LINE S'''
    if len(p) == 3:
        p[0] = ('statement', p[1], p[2])
    else:
        p[0] = ('statement', p[1], p[3])


def p_statement(p):
    'S : statement END_LINE'
    p[0] = p[1]


def p_declarations(p):
    'statement : declarations'
    p[0] = p[1]


# =================================
# ||       declarations          ||
# =================================

def p_variables(p):
    '''declarations : VAR ID ASSIGN expr
                    | VAR ID ASSIGN relexpr
                    | VAR ID'''
    if(len(p) > 3):
        p[0] = ('VAR', p[2], p[4])
    else:
        p[0] = ('VAR', p[2])


def p_write(p):
    'declarations : WRITE LPAREN expr RPAREN'
    p[0] = ('WRITE', p[3])


# =================================
# ||       expressions           ||
# =================================

def p_binary_expression(p):
    '''expr : expr PLUS expr
            | expr MINUS expr
            | expr TIMES expr
            | expr DIVIDE expr
            | expr MOD expr'''
    p[0] = ('BINOP', p[2], p[1], p[3])


def p_number_expression(p):
    '''expr : NUMBER
    '''
    p[0] = ('NUMBER', p[1])


def p_string_expression(p):
    'expr : STRINGS'
    p[0] = ('STRINGS', p[1])

def p_group_expression(p):
    '''expr : LPAREN expr RPAREN'''
    p[0] = ('GROUP', p[2])


# =================================
# ||   relational expressions    ||
# =================================

def p_relational_expressions(p):
    '''relexpr : expr LT expr
               | expr LE expr
               | expr GT expr
               | expr GE expr
               | expr EQUALS expr
               | expr NE expr'''
    p[0] = ('RELOP', p[2], p[1], p[3])


parser = yacc.yacc()
file = open('input.js')
code = file.read()
file.close()
result = parser.parse(code)
print(result)
