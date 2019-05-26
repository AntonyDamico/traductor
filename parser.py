from lexer import tokens
import ply.yacc as yacc
import sys

precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'ASSIGN', 'NE'),
    ('left', 'GE', 'LE', 'LT', 'GT'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE', 'MOD'),
    ('right', 'NOT'),
    ('left', 'INCREMENT', 'DECREMENT')
)


# =================================
# ||        Statements           ||
# =================================

def p_rec_statement(p):
    '''S : statement S
         | statement END_LINE S'''
    if len(p) == 3:
        p[0] = (p[1], p[2])
    else:
        p[0] = (p[1], p[3])


def p_statement(p):
    '''S : statement END_LINE
                 | command
                 | command END_LINE
                 | ifcommand'''
    p[0] = p[1]


def p_declarations(p):
    '''statement : declarations'''
    p[0] = p[1]


def p_expr_statement(p):
    '''statement : expr'''
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


# =================================
# ||        Commands             ||
# =================================

def p_write(p):
    'command : WRITE LPAREN expr RPAREN'
    p[0] = ('WRITE', p[3])


def p_command_while(p):
    '''command : WHILE LPAREN expr RPAREN LBRACKET S RBRACKET
               | WHILE LPAREN relexpr RPAREN LBRACKET S RBRACKET'''
    p[0] = ('WHILE', p[3], p[6])


def p_command_for(p):
    ''' command : FOR LPAREN declarations END_LINE relexpr END_LINE expr RPAREN LBRACKET S RBRACKET
    '''
    p[0] = ('FOR', p[3], p[5], p[7], p[10])

# def p_command_if(p):
    # if(len(p) > 8):
    #     p[0] =('IF', p[3], p[6], 'ELSE', p[10])
    # else:
    #     p[0] = ('IF', p[3], p[6])


def p_if(p):
    ''' ifcommand : IF LPAREN relexprgroup RPAREN LBRACKET S RBRACKET
                    | IF LPAREN relexprgroup RPAREN LBRACKET S RBRACKET ELSE ifcommand 
                    | IF LPAREN relexprgroup RPAREN LBRACKET S RBRACKET ELSE LBRACKET S RBRACKET '''
    if(len(p) > 11):
        p[0] = ('IF', p[3], p[6], 'ELSE', p[10])
    elif(len(p) > 8):
        p[0] = ('IF', p[3], p[6], 'ELSE', p[9])
    else:
        p[0] = ('IF', p[3], p[6])


# =================================
# ||       expressions           ||
# =================================

def p_binary_expression(p):
    '''expr : expr PLUS expr
            | expr MINUS expr
            | expr TIMES expr
            | expr DIVIDE expr
            | expr MOD expr'''
    if(len(p) > 3):
        p[0] = ('BINOP', p[2], p[1], p[3])
    # else:
        # p[0] = ('UNARY', p[2], p[1])


def p_unary_expressions(p):
    '''expr : expr INCREMENT
            | expr DECREMENT'''
    p[0] = ('UNARY', p[2], p[1])


def p_assign_expression(p):
    '''expr : ID ASSIGN expr'''
    p[0] = ('ASSIGN', p[1], p[3])


def p_number_expression(p):
    '''expr : NUMBER'''
    p[0] = ('NUMBER', p[1])


def p_string_expression(p):
    'expr : STRINGS'
    p[0] = ('STRINGS', p[1])


def p_variable_expression(p):
    'expr : ID'
    if(p[1] in ['true', 'false']):
        p[0] = ('BOOL', p[1])
    else:
        p[0] = ('ID', p[1])


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


def p_rel_group(p):
    '''relexprgroup : relexpr AND relexprgroup
                    | relexpr OR relexprgroup
                    | relexpr
                    | expr
    '''
    if(len(p) > 3):
        p[0] = ('RELOPS', p[2], p[1], p[3])
    elif(len(p) > 2):
        p[0] = ('NOT', p[2])
    else:
        p[0] = p[1]


# =================================
# ||         Commands            ||
# =================================

parser = yacc.yacc()
file = open('input.js')
code = file.read()
file.close()
result = parser.parse(code)
print(result)
