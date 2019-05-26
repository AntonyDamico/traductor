
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftORleftANDleftASSIGNNEleftGELELTGTleftPLUSMINUSleftTIMESDIVIDEMODrightNOTleftINCREMENTDECREMENTAND ASSIGN COMMA DECREMENT DIVIDE ELSE END_LINE EQUALS FOR FUNCTION GE GT ID IF INCREMENT LBRACKET LE LPAREN LT MINUS MOD NE NOT NUMBER OR PLUS PROMPT QUOTE RBRACKET RETURN RPAREN STRINGS TIMES VAR WHILE WRITES : statement S\n         | statement END_LINE SS : statement END_LINE\n                 | command\n                 | command END_LINEstatement : declarationsstatement : exprdeclarations : VAR ID ASSIGN expr\n                    | VAR ID ASSIGN relexpr\n                    | VAR IDcommand : WRITE LPAREN expr RPARENcommand : WHILE LPAREN expr RPAREN LBRACKET S RBRACKET\n               | WHILE LPAREN relexpr RPAREN LBRACKET S RBRACKET command : FOR LPAREN declarations END_LINE relexpr END_LINE expr RPAREN LBRACKET S RBRACKET\n     command : IF LPAREN relexprgroup RPAREN LBRACKET S RBRACKETexpr : expr PLUS expr\n            | expr MINUS expr\n            | expr TIMES expr\n            | expr DIVIDE expr\n            | expr MOD exprexpr : expr INCREMENT\n            | expr DECREMENTexpr : ID ASSIGN exprexpr : NUMBERexpr : STRINGSexpr : IDexpr : LPAREN expr RPARENrelexpr : expr LT expr\n               | expr LE expr\n               | expr GT expr\n               | expr GE expr\n               | expr EQUALS expr\n               | expr NE exprrelexprgroup : relexpr AND relexprgroup\n                    | relexpr OR relexprgroup\n                    | relexpr \n    '
    
_lr_action_items = {'NUMBER':([0,1,3,4,8,10,12,13,15,17,19,21,22,23,24,25,26,27,28,29,30,37,38,39,43,44,45,46,47,49,50,52,53,54,55,56,58,59,61,62,63,64,65,66,67,68,69,70,72,77,84,],[1,-24,-25,1,1,-26,-7,-6,1,1,1,-10,1,1,1,1,1,-21,-22,1,1,-27,1,-23,-19,-18,-16,-17,-20,1,1,1,1,1,1,1,-9,-8,1,1,1,-32,-30,1,-28,-29,-31,-33,1,1,1,]),'LBRACKET':([48,51,60,83,],[63,66,72,84,]),'WHILE':([0,1,3,4,10,12,13,17,21,27,28,37,39,43,44,45,46,47,58,59,63,64,65,66,67,68,69,70,72,84,],[2,-24,-25,2,-26,-7,-6,2,-10,-21,-22,-27,-23,-19,-18,-16,-17,-20,-9,-8,2,-32,-30,2,-28,-29,-31,-33,2,2,]),'MINUS':([1,3,10,12,20,27,28,33,36,37,39,42,43,44,45,46,47,59,64,65,67,68,69,70,81,],[-24,-25,-26,29,29,-21,-22,29,29,-27,29,29,-19,-18,-16,-17,-20,29,29,29,29,29,29,29,29,]),'LE':([1,3,10,27,28,33,37,39,42,43,44,45,46,47,59,],[-24,-25,-26,-21,-22,53,-27,-23,53,-19,-18,-16,-17,-20,53,]),'RPAREN':([1,3,10,20,27,28,32,33,36,37,39,40,41,43,44,45,46,47,64,65,67,68,69,70,73,74,81,],[-24,-25,-26,37,-21,-22,48,51,57,-27,-23,60,-36,-19,-18,-16,-17,-20,-32,-30,-28,-29,-31,-33,-34,-35,83,]),'NE':([1,3,10,27,28,33,37,39,42,43,44,45,46,47,59,],[-24,-25,-26,-21,-22,55,-27,-23,55,-19,-18,-16,-17,-20,55,]),'STRINGS':([0,1,3,4,8,10,12,13,15,17,19,21,22,23,24,25,26,27,28,29,30,37,38,39,43,44,45,46,47,49,50,52,53,54,55,56,58,59,61,62,63,64,65,66,67,68,69,70,72,77,84,],[3,-24,-25,3,3,-26,-7,-6,3,3,3,-10,3,3,3,3,3,-21,-22,3,3,-27,3,-23,-19,-18,-16,-17,-20,3,3,3,3,3,3,3,-9,-8,3,3,3,-32,-30,3,-28,-29,-31,-33,3,3,3,]),'LT':([1,3,10,27,28,33,37,39,42,43,44,45,46,47,59,],[-24,-25,-26,-21,-22,52,-27,-23,52,-19,-18,-16,-17,-20,52,]),'PLUS':([1,3,10,12,20,27,28,33,36,37,39,42,43,44,45,46,47,59,64,65,67,68,69,70,81,],[-24,-25,-26,26,26,-21,-22,26,26,-27,26,26,-19,-18,-16,-17,-20,26,26,26,26,26,26,26,26,]),'INCREMENT':([1,3,10,12,20,27,28,33,36,37,39,42,43,44,45,46,47,59,64,65,67,68,69,70,81,],[-24,-25,-26,27,27,-21,-22,27,27,-27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,]),'ASSIGN':([10,21,],[22,38,]),'$end':([7,14,16,17,31,34,57,79,80,82,86,],[0,-4,-1,-3,-5,-2,-11,-13,-12,-15,-14,]),'RBRACKET':([14,16,17,31,34,57,75,76,78,79,80,82,85,86,],[-4,-1,-3,-5,-2,-11,79,80,82,-13,-12,-15,86,-14,]),'GT':([1,3,10,27,28,33,37,39,42,43,44,45,46,47,59,],[-24,-25,-26,-21,-22,50,-27,-23,50,-19,-18,-16,-17,-20,50,]),'DIVIDE':([1,3,10,12,20,27,28,33,36,37,39,42,43,44,45,46,47,59,64,65,67,68,69,70,81,],[-24,-25,-26,24,24,-21,-22,24,24,-27,24,24,-19,-18,24,24,-20,24,24,24,24,24,24,24,24,]),'FOR':([0,1,3,4,10,12,13,17,21,27,28,37,39,43,44,45,46,47,58,59,63,64,65,66,67,68,69,70,72,84,],[5,-24,-25,5,-26,-7,-6,5,-10,-21,-22,-27,-23,-19,-18,-16,-17,-20,-9,-8,5,-32,-30,5,-28,-29,-31,-33,5,5,]),'EQUALS':([1,3,10,27,28,33,37,39,42,43,44,45,46,47,59,],[-24,-25,-26,-21,-22,49,-27,-23,49,-19,-18,-16,-17,-20,49,]),'TIMES':([1,3,10,12,20,27,28,33,36,37,39,42,43,44,45,46,47,59,64,65,67,68,69,70,81,],[-24,-25,-26,25,25,-21,-22,25,25,-27,25,25,-19,-18,25,25,-20,25,25,25,25,25,25,25,25,]),'WRITE':([0,1,3,4,10,12,13,17,21,27,28,37,39,43,44,45,46,47,58,59,63,64,65,66,67,68,69,70,72,84,],[6,-24,-25,6,-26,-7,-6,6,-10,-21,-22,-27,-23,-19,-18,-16,-17,-20,-9,-8,6,-32,-30,6,-28,-29,-31,-33,6,6,]),'GE':([1,3,10,27,28,33,37,39,42,43,44,45,46,47,59,],[-24,-25,-26,-21,-22,54,-27,-23,54,-19,-18,-16,-17,-20,54,]),'END_LINE':([1,3,4,10,12,13,14,21,27,28,35,37,39,43,44,45,46,47,57,58,59,64,65,67,68,69,70,71,79,80,82,86,],[-24,-25,17,-26,-7,-6,31,-10,-21,-22,56,-27,-23,-19,-18,-16,-17,-20,-11,-9,-8,-32,-30,-28,-29,-31,-33,77,-13,-12,-15,-14,]),'LPAREN':([0,1,2,3,4,5,6,8,10,11,12,13,15,17,19,21,22,23,24,25,26,27,28,29,30,37,38,39,43,44,45,46,47,49,50,52,53,54,55,56,58,59,61,62,63,64,65,66,67,68,69,70,72,77,84,],[8,-24,15,-25,8,18,19,8,-26,23,-7,-6,8,8,8,-10,8,8,8,8,8,-21,-22,8,8,-27,8,-23,-19,-18,-16,-17,-20,8,8,8,8,8,8,8,-9,-8,8,8,8,-32,-30,8,-28,-29,-31,-33,8,8,8,]),'VAR':([0,1,3,4,10,12,13,17,18,21,27,28,37,39,43,44,45,46,47,58,59,63,64,65,66,67,68,69,70,72,84,],[9,-24,-25,9,-26,-7,-6,9,9,-10,-21,-22,-27,-23,-19,-18,-16,-17,-20,-9,-8,9,-32,-30,9,-28,-29,-31,-33,9,9,]),'ID':([0,1,3,4,8,9,10,12,13,15,17,19,21,22,23,24,25,26,27,28,29,30,37,38,39,43,44,45,46,47,49,50,52,53,54,55,56,58,59,61,62,63,64,65,66,67,68,69,70,72,77,84,],[10,-24,-25,10,10,21,-26,-7,-6,10,10,10,-10,10,10,10,10,10,-21,-22,10,10,-27,10,-23,-19,-18,-16,-17,-20,10,10,10,10,10,10,10,-9,-8,10,10,10,-32,-30,10,-28,-29,-31,-33,10,10,10,]),'IF':([0,1,3,4,10,12,13,17,21,27,28,37,39,43,44,45,46,47,58,59,63,64,65,66,67,68,69,70,72,84,],[11,-24,-25,11,-26,-7,-6,11,-10,-21,-22,-27,-23,-19,-18,-16,-17,-20,-9,-8,11,-32,-30,11,-28,-29,-31,-33,11,11,]),'AND':([1,3,10,27,28,37,39,41,43,44,45,46,47,64,65,67,68,69,70,],[-24,-25,-26,-21,-22,-27,-23,61,-19,-18,-16,-17,-20,-32,-30,-28,-29,-31,-33,]),'DECREMENT':([1,3,10,12,20,27,28,33,36,37,39,42,43,44,45,46,47,59,64,65,67,68,69,70,81,],[-24,-25,-26,28,28,-21,-22,28,28,-27,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,]),'OR':([1,3,10,27,28,37,39,41,43,44,45,46,47,64,65,67,68,69,70,],[-24,-25,-26,-21,-22,-27,-23,62,-19,-18,-16,-17,-20,-32,-30,-28,-29,-31,-33,]),'MOD':([1,3,10,12,20,27,28,33,36,37,39,42,43,44,45,46,47,59,64,65,67,68,69,70,81,],[-24,-25,-26,30,30,-21,-22,30,30,-27,30,30,-19,-18,30,30,-20,30,30,30,30,30,30,30,30,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'relexpr':([15,23,38,56,61,62,],[32,41,58,71,41,41,]),'expr':([0,4,8,15,17,19,22,23,24,25,26,29,30,38,49,50,52,53,54,55,56,61,62,63,66,72,77,84,],[12,12,20,33,12,36,39,42,43,44,45,46,47,59,64,65,67,68,69,70,42,42,42,12,12,12,81,12,]),'declarations':([0,4,17,18,63,66,72,84,],[13,13,13,35,13,13,13,13,]),'S':([0,4,17,63,66,72,84,],[7,16,34,75,76,78,85,]),'command':([0,4,17,63,66,72,84,],[14,14,14,14,14,14,14,]),'statement':([0,4,17,63,66,72,84,],[4,4,4,4,4,4,4,]),'relexprgroup':([23,61,62,],[40,73,74,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> S","S'",1,None,None,None),
  ('S -> statement S','S',2,'p_rec_statement','parser.py',22),
  ('S -> statement END_LINE S','S',3,'p_rec_statement','parser.py',23),
  ('S -> statement END_LINE','S',2,'p_statement','parser.py',31),
  ('S -> command','S',1,'p_statement','parser.py',32),
  ('S -> command END_LINE','S',2,'p_statement','parser.py',33),
  ('statement -> declarations','statement',1,'p_declarations','parser.py',38),
  ('statement -> expr','statement',1,'p_expr_statement','parser.py',43),
  ('declarations -> VAR ID ASSIGN expr','declarations',4,'p_variables','parser.py',52),
  ('declarations -> VAR ID ASSIGN relexpr','declarations',4,'p_variables','parser.py',53),
  ('declarations -> VAR ID','declarations',2,'p_variables','parser.py',54),
  ('command -> WRITE LPAREN expr RPAREN','command',4,'p_write','parser.py',66),
  ('command -> WHILE LPAREN expr RPAREN LBRACKET S RBRACKET','command',7,'p_command_while','parser.py',71),
  ('command -> WHILE LPAREN relexpr RPAREN LBRACKET S RBRACKET','command',7,'p_command_while','parser.py',72),
  ('command -> FOR LPAREN declarations END_LINE relexpr END_LINE expr RPAREN LBRACKET S RBRACKET','command',11,'p_command_for','parser.py',77),
  ('command -> IF LPAREN relexprgroup RPAREN LBRACKET S RBRACKET','command',7,'p_command_if','parser.py',82),
  ('expr -> expr PLUS expr','expr',3,'p_binary_expression','parser.py',91),
  ('expr -> expr MINUS expr','expr',3,'p_binary_expression','parser.py',92),
  ('expr -> expr TIMES expr','expr',3,'p_binary_expression','parser.py',93),
  ('expr -> expr DIVIDE expr','expr',3,'p_binary_expression','parser.py',94),
  ('expr -> expr MOD expr','expr',3,'p_binary_expression','parser.py',95),
  ('expr -> expr INCREMENT','expr',2,'p_unary_expressions','parser.py',103),
  ('expr -> expr DECREMENT','expr',2,'p_unary_expressions','parser.py',104),
  ('expr -> ID ASSIGN expr','expr',3,'p_assign_expression','parser.py',109),
  ('expr -> NUMBER','expr',1,'p_number_expression','parser.py',114),
  ('expr -> STRINGS','expr',1,'p_string_expression','parser.py',119),
  ('expr -> ID','expr',1,'p_variable_expression','parser.py',124),
  ('expr -> LPAREN expr RPAREN','expr',3,'p_group_expression','parser.py',129),
  ('relexpr -> expr LT expr','relexpr',3,'p_relational_expressions','parser.py',138),
  ('relexpr -> expr LE expr','relexpr',3,'p_relational_expressions','parser.py',139),
  ('relexpr -> expr GT expr','relexpr',3,'p_relational_expressions','parser.py',140),
  ('relexpr -> expr GE expr','relexpr',3,'p_relational_expressions','parser.py',141),
  ('relexpr -> expr EQUALS expr','relexpr',3,'p_relational_expressions','parser.py',142),
  ('relexpr -> expr NE expr','relexpr',3,'p_relational_expressions','parser.py',143),
  ('relexprgroup -> relexpr AND relexprgroup','relexprgroup',3,'p_rel_group','parser.py',148),
  ('relexprgroup -> relexpr OR relexprgroup','relexprgroup',3,'p_rel_group','parser.py',149),
  ('relexprgroup -> relexpr','relexprgroup',1,'p_rel_group','parser.py',150),
]
