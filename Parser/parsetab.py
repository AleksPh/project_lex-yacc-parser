
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftTIMESDIVIDEnonassocUMINUSleftEXPONENTDIVIDE EQUALS EXPONENT IDENTIFIER LPAREN MINUS NUMBER PLUS RPAREN TIMES\n    statement : assignment\n              | expression\n    assignment : IDENTIFIER EQUALS expressionexpression : expression PLUS expression\n                  | expression MINUS expression\n                  | expression TIMES expression\n                  | expression DIVIDE expressionexpression : MINUS expression %prec UMINUSexpression : LPAREN expression RPARENexpression : NUMBERexpression : expression EXPONENT expressionexpression : IDENTIFIER'
    
_lr_action_items = {'IDENTIFIER':([0,5,6,8,9,10,11,12,13,],[4,15,15,15,15,15,15,15,15,]),'MINUS':([0,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,],[5,9,-12,5,5,-10,5,5,5,5,5,5,-8,-12,9,-4,-5,-6,-7,-11,9,-9,]),'LPAREN':([0,5,6,8,9,10,11,12,13,],[6,6,6,6,6,6,6,6,6,]),'NUMBER':([0,5,6,8,9,10,11,12,13,],[7,7,7,7,7,7,7,7,7,]),'$end':([1,2,3,4,7,14,15,17,18,19,20,21,22,23,],[0,-1,-2,-12,-10,-8,-12,-4,-5,-6,-7,-11,-3,-9,]),'PLUS':([3,4,7,14,15,16,17,18,19,20,21,22,23,],[8,-12,-10,-8,-12,8,-4,-5,-6,-7,-11,8,-9,]),'TIMES':([3,4,7,14,15,16,17,18,19,20,21,22,23,],[10,-12,-10,-8,-12,10,10,10,-6,-7,-11,10,-9,]),'DIVIDE':([3,4,7,14,15,16,17,18,19,20,21,22,23,],[11,-12,-10,-8,-12,11,11,11,-6,-7,-11,11,-9,]),'EXPONENT':([3,4,7,14,15,16,17,18,19,20,21,22,23,],[12,-12,-10,12,-12,12,12,12,12,12,-11,12,-9,]),'EQUALS':([4,],[13,]),'RPAREN':([7,14,15,16,17,18,19,20,21,23,],[-10,-8,-12,23,-4,-5,-6,-7,-11,-9,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,],[1,]),'assignment':([0,],[2,]),'expression':([0,5,6,8,9,10,11,12,13,],[3,14,16,17,18,19,20,21,22,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> assignment','statement',1,'p_statement','yacc_grammar.py',18),
  ('statement -> expression','statement',1,'p_statement','yacc_grammar.py',19),
  ('assignment -> IDENTIFIER EQUALS expression','assignment',3,'p_assignment','yacc_grammar.py',25),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop','yacc_grammar.py',34),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop','yacc_grammar.py',35),
  ('expression -> expression TIMES expression','expression',3,'p_expression_binop','yacc_grammar.py',36),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_binop','yacc_grammar.py',37),
  ('expression -> MINUS expression','expression',2,'p_expression_uminus','yacc_grammar.py',49),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_group','yacc_grammar.py',54),
  ('expression -> NUMBER','expression',1,'p_expression_number','yacc_grammar.py',59),
  ('expression -> expression EXPONENT expression','expression',3,'p_expression_exponent','yacc_grammar.py',64),
  ('expression -> IDENTIFIER','expression',1,'p_expression_var','yacc_grammar.py',77),
]
