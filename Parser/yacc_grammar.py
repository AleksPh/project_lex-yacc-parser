import ply.yacc as yacc 
from Parser.lex import tokens
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('nonassoc', 'UMINUS'),  
    ('left', 'EXPONENT'),
)

variables = {}

def p_statement(p):
    '''
    statement : assignment
              | expression
    '''
    p[0] = p[1]


def p_assignment(p):
    'assignment : IDENTIFIER EQUALS expression'
    variables[p[1]] = p[3]
    p[0] = p[3]

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]


def p_expression_uminus(p):
    "expression : MINUS expression %prec UMINUS"
    p[0] = -p[2]


def p_expression_group(p):
    "expression : LPAREN expression RPAREN"
    p[0] = p[2]


def p_expression_number(p):
    "expression : NUMBER"
    p[0] = p[1]


def p_expression_exponent(p):
    'expression : expression EXPONENT expression'
    p[0] = p[1] ** p[3]


def p_error(p):
    print("Syntax error in input!")


def p_expression_var(p):
    'expression : IDENTIFIER'
    try:
        p[0] = variables[p[1]]
    except LookupError:
        print(f"Undefined name '{p[1]}'")
        p[0] = 0


parser = yacc.yacc()