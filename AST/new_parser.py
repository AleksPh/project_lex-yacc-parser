import ply.yacc as yacc
from AST.ast_nodes import BinOpNode, NumNode, VarNode
from AST.new_lexer import tokens
precedence = (('left', 'PLUS', 'MINUS'), ('left', 'TIMES', 'DIVIDE'), ('right', 'EXPONENT'))

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression EXPONENT expression'''
    p[0] = BinOpNode(left=p[1], operator=p[2], right=p[3])

def p_expression_number(p):
    "expression : NUMBER"
    p[0] = NumNode(p[1])

def p_expression_paren(p):
    "expression : LPAREN expression RPAREN"
    p[0] = p[2]

def p_expression_var(p):
    "expression : IDENTIFIER"
    p[0] = VarNode(p[1])

def p_error(p):
    pass

new_parser = yacc.yacc()