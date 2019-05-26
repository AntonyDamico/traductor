
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftORleftANDleftASSIGNNEleftGELELTGTleftPLUSMINUSleftTIMESDIVIDEMODrightNOTleftINCREMENTDECREMENTAND ASSIGN COMMA DECREMENT DIVIDE ELSE END_LINE EQUALS FOR FUNCTION GE GT ID IF INCREMENT LBRACKET LE LPAREN LT MINUS MOD NE NOT NUMBER OR PLUS PROMPT QUOTE RBRACKET RETURN RPAREN STRINGS TIMES VAR WHILE WRITES : statement S\n         | statement END_LINE SS : statement END_LINE\n                 | command\n                 | command END_LINE\n                 | ifcommandstatement : declarationsstatement : exprdeclarations : VAR ID ASSIGN expr\n                    | VAR ID ASSIGN relexpr\n                    | VAR IDcommand : WRITE LPAREN expr RPARENcommand : WHILE LPAREN expr RPAREN LBRACKET S RBRACKET\n               | WHILE LPAREN relexpr RPAREN LBRACKET S RBRACKET command : FOR LPAREN declarations END_LINE relexpr END_LINE expr RPAREN LBRACKET S RBRACKET\n     ifcommand : IF LPAREN relexprgroup RPAREN LBRACKET S RBRACKET\n                    | IF LPAREN relexprgroup RPAREN LBRACKET S RBRACKET ELSE ifcommand \n                    | IF LPAREN relexprgroup RPAREN LBRACKET S RBRACKET ELSE LBRACKET S RBRACKET expr : expr PLUS expr\n            | expr MINUS expr\n            | expr TIMES expr\n            | expr DIVIDE expr\n            | expr MOD exprexpr : expr INCREMENT\n            | expr DECREMENTexpr : ID ASSIGN exprexpr : NUMBERexpr : STRINGSexpr : IDexpr : LPAREN expr RPARENrelexpr : expr LT expr\n               | expr LE expr\n               | expr GT expr\n               | expr GE expr\n               | expr EQUALS expr\n               | expr NE exprrelexprgroup : relexpr AND relexprgroup\n                    | relexpr OR relexprgroup\n                    | relexpr \n    '
    
_lr_action_items = {'NUMBER':([0,1,3,4,9,11,13,14,16,18,20,22,23,24,25,26,27,28,29,30,31,38,39,40,44,45,46,47,48,50,51,53,54,55,56,57,59,60,62,63,64,65,66,67,68,69,70,71,73,78,86,88,],[1,-27,-28,1,1,-29,-8,-7,1,1,1,-11,1,1,1,1,1,-24,-25,1,1,-30,1,-26,-22,-21,-19,-20,-23,1,1,1,1,1,1,1,-10,-9,1,1,1,-35,-33,1,-31,-32,-34,-36,1,1,1,1,]),'LBRACKET':([49,52,61,84,85,],[64,67,73,86,88,]),'WHILE':([0,1,3,4,11,13,14,18,22,28,29,38,40,44,45,46,47,48,59,60,64,65,66,67,68,69,70,71,73,86,88,],[2,-27,-28,2,-29,-8,-7,2,-11,-24,-25,-30,-26,-22,-21,-19,-20,-23,-10,-9,2,-35,-33,2,-31,-32,-34,-36,2,2,2,]),'MINUS':([1,3,11,13,21,28,29,34,37,38,40,43,44,45,46,47,48,60,65,66,68,69,70,71,82,],[-27,-28,-29,30,30,-24,-25,30,30,-30,30,30,-22,-21,-19,-20,-23,30,30,30,30,30,30,30,30,]),'LE':([1,3,11,28,29,34,38,40,43,44,45,46,47,48,60,],[-27,-28,-29,-24,-25,54,-30,-26,54,-22,-21,-19,-20,-23,54,]),'RPAREN':([1,3,11,21,28,29,33,34,37,38,40,41,42,44,45,46,47,48,65,66,68,69,70,71,74,75,82,],[-27,-28,-29,38,-24,-25,49,52,58,-30,-26,61,-39,-22,-21,-19,-20,-23,-35,-33,-31,-32,-34,-36,-37,-38,84,]),'NE':([1,3,11,28,29,34,38,40,43,44,45,46,47,48,60,],[-27,-28,-29,-24,-25,56,-30,-26,56,-22,-21,-19,-20,-23,56,]),'STRINGS':([0,1,3,4,9,11,13,14,16,18,20,22,23,24,25,26,27,28,29,30,31,38,39,40,44,45,46,47,48,50,51,53,54,55,56,57,59,60,62,63,64,65,66,67,68,69,70,71,73,78,86,88,],[3,-27,-28,3,3,-29,-8,-7,3,3,3,-11,3,3,3,3,3,-24,-25,3,3,-30,3,-26,-22,-21,-19,-20,-23,3,3,3,3,3,3,3,-10,-9,3,3,3,-35,-33,3,-31,-32,-34,-36,3,3,3,3,]),'LT':([1,3,11,28,29,34,38,40,43,44,45,46,47,48,60,],[-27,-28,-29,-24,-25,53,-30,-26,53,-22,-21,-19,-20,-23,53,]),'PLUS':([1,3,11,13,21,28,29,34,37,38,40,43,44,45,46,47,48,60,65,66,68,69,70,71,82,],[-27,-28,-29,27,27,-24,-25,27,27,-30,27,27,-22,-21,-19,-20,-23,27,27,27,27,27,27,27,27,]),'INCREMENT':([1,3,11,13,21,28,29,34,37,38,40,43,44,45,46,47,48,60,65,66,68,69,70,71,82,],[-27,-28,-29,28,28,-24,-25,28,28,-30,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,]),'ASSIGN':([11,22,],[23,39,]),'$end':([5,8,15,17,18,32,35,58,80,81,83,87,91,92,],[-6,0,-4,-1,-3,-5,-2,-12,-14,-13,-16,-17,-15,-18,]),'RBRACKET':([5,15,17,18,32,35,58,76,77,79,80,81,83,87,89,90,91,92,],[-6,-4,-1,-3,-5,-2,-12,80,81,83,-14,-13,-16,-17,91,92,-15,-18,]),'GT':([1,3,11,28,29,34,38,40,43,44,45,46,47,48,60,],[-27,-28,-29,-24,-25,51,-30,-26,51,-22,-21,-19,-20,-23,51,]),'DIVIDE':([1,3,11,13,21,28,29,34,37,38,40,43,44,45,46,47,48,60,65,66,68,69,70,71,82,],[-27,-28,-29,25,25,-24,-25,25,25,-30,25,25,-22,-21,25,25,-23,25,25,25,25,25,25,25,25,]),'FOR':([0,1,3,4,11,13,14,18,22,28,29,38,40,44,45,46,47,48,59,60,64,65,66,67,68,69,70,71,73,86,88,],[6,-27,-28,6,-29,-8,-7,6,-11,-24,-25,-30,-26,-22,-21,-19,-20,-23,-10,-9,6,-35,-33,6,-31,-32,-34,-36,6,6,6,]),'EQUALS':([1,3,11,28,29,34,38,40,43,44,45,46,47,48,60,],[-27,-28,-29,-24,-25,50,-30,-26,50,-22,-21,-19,-20,-23,50,]),'TIMES':([1,3,11,13,21,28,29,34,37,38,40,43,44,45,46,47,48,60,65,66,68,69,70,71,82,],[-27,-28,-29,26,26,-24,-25,26,26,-30,26,26,-22,-21,26,26,-23,26,26,26,26,26,26,26,26,]),'WRITE':([0,1,3,4,11,13,14,18,22,28,29,38,40,44,45,46,47,48,59,60,64,65,66,67,68,69,70,71,73,86,88,],[7,-27,-28,7,-29,-8,-7,7,-11,-24,-25,-30,-26,-22,-21,-19,-20,-23,-10,-9,7,-35,-33,7,-31,-32,-34,-36,7,7,7,]),'GE':([1,3,11,28,29,34,38,40,43,44,45,46,47,48,60,],[-27,-28,-29,-24,-25,55,-30,-26,55,-22,-21,-19,-20,-23,55,]),'END_LINE':([1,3,4,11,13,14,15,22,28,29,36,38,40,44,45,46,47,48,58,59,60,65,66,68,69,70,71,72,80,81,91,],[-27,-28,18,-29,-8,-7,32,-11,-24,-25,57,-30,-26,-22,-21,-19,-20,-23,-12,-10,-9,-35,-33,-31,-32,-34,-36,78,-14,-13,-15,]),'LPAREN':([0,1,2,3,4,6,7,9,11,12,13,14,16,18,20,22,23,24,25,26,27,28,29,30,31,38,39,40,44,45,46,47,48,50,51,53,54,55,56,57,59,60,62,63,64,65,66,67,68,69,70,71,73,78,86,88,],[9,-27,16,-28,9,19,20,9,-29,24,-8,-7,9,9,9,-11,9,9,9,9,9,-24,-25,9,9,-30,9,-26,-22,-21,-19,-20,-23,9,9,9,9,9,9,9,-10,-9,9,9,9,-35,-33,9,-31,-32,-34,-36,9,9,9,9,]),'VAR':([0,1,3,4,11,13,14,18,19,22,28,29,38,40,44,45,46,47,48,59,60,64,65,66,67,68,69,70,71,73,86,88,],[10,-27,-28,10,-29,-8,-7,10,10,-11,-24,-25,-30,-26,-22,-21,-19,-20,-23,-10,-9,10,-35,-33,10,-31,-32,-34,-36,10,10,10,]),'ELSE':([83,],[85,]),'ID':([0,1,3,4,9,10,11,13,14,16,18,20,22,23,24,25,26,27,28,29,30,31,38,39,40,44,45,46,47,48,50,51,53,54,55,56,57,59,60,62,63,64,65,66,67,68,69,70,71,73,78,86,88,],[11,-27,-28,11,11,22,-29,-8,-7,11,11,11,-11,11,11,11,11,11,-24,-25,11,11,-30,11,-26,-22,-21,-19,-20,-23,11,11,11,11,11,11,11,-10,-9,11,11,11,-35,-33,11,-31,-32,-34,-36,11,11,11,11,]),'IF':([0,1,3,4,11,13,14,18,22,28,29,38,40,44,45,46,47,48,59,60,64,65,66,67,68,69,70,71,73,85,86,88,],[12,-27,-28,12,-29,-8,-7,12,-11,-24,-25,-30,-26,-22,-21,-19,-20,-23,-10,-9,12,-35,-33,12,-31,-32,-34,-36,12,12,12,12,]),'AND':([1,3,11,28,29,38,40,42,44,45,46,47,48,65,66,68,69,70,71,],[-27,-28,-29,-24,-25,-30,-26,62,-22,-21,-19,-20,-23,-35,-33,-31,-32,-34,-36,]),'DECREMENT':([1,3,11,13,21,28,29,34,37,38,40,43,44,45,46,47,48,60,65,66,68,69,70,71,82,],[-27,-28,-29,29,29,-24,-25,29,29,-30,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'OR':([1,3,11,28,29,38,40,42,44,45,46,47,48,65,66,68,69,70,71,],[-27,-28,-29,-24,-25,-30,-26,63,-22,-21,-19,-20,-23,-35,-33,-31,-32,-34,-36,]),'MOD':([1,3,11,13,21,28,29,34,37,38,40,43,44,45,46,47,48,60,65,66,68,69,70,71,82,],[-27,-28,-29,31,31,-24,-25,31,31,-30,31,31,-22,-21,31,31,-23,31,31,31,31,31,31,31,31,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'relexpr':([16,24,39,57,62,63,],[33,42,59,72,42,42,]),'ifcommand':([0,4,18,64,67,73,85,86,88,],[5,5,5,5,5,5,87,5,5,]),'expr':([0,4,9,16,18,20,23,24,25,26,27,30,31,39,50,51,53,54,55,56,57,62,63,64,67,73,78,86,88,],[13,13,21,34,13,37,40,43,44,45,46,47,48,60,65,66,68,69,70,71,43,43,43,13,13,13,82,13,13,]),'declarations':([0,4,18,19,64,67,73,86,88,],[14,14,14,36,14,14,14,14,14,]),'S':([0,4,18,64,67,73,86,88,],[8,17,35,76,77,79,89,90,]),'command':([0,4,18,64,67,73,86,88,],[15,15,15,15,15,15,15,15,]),'statement':([0,4,18,64,67,73,86,88,],[4,4,4,4,4,4,4,4,]),'relexprgroup':([24,62,63,],[41,74,75,]),}

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
  ('S -> ifcommand','S',1,'p_statement','parser.py',34),
  ('statement -> declarations','statement',1,'p_declarations','parser.py',39),
  ('statement -> expr','statement',1,'p_expr_statement','parser.py',44),
  ('declarations -> VAR ID ASSIGN expr','declarations',4,'p_variables','parser.py',53),
  ('declarations -> VAR ID ASSIGN relexpr','declarations',4,'p_variables','parser.py',54),
  ('declarations -> VAR ID','declarations',2,'p_variables','parser.py',55),
  ('command -> WRITE LPAREN expr RPAREN','command',4,'p_write','parser.py',67),
  ('command -> WHILE LPAREN expr RPAREN LBRACKET S RBRACKET','command',7,'p_command_while','parser.py',72),
  ('command -> WHILE LPAREN relexpr RPAREN LBRACKET S RBRACKET','command',7,'p_command_while','parser.py',73),
  ('command -> FOR LPAREN declarations END_LINE relexpr END_LINE expr RPAREN LBRACKET S RBRACKET','command',11,'p_command_for','parser.py',78),
  ('ifcommand -> IF LPAREN relexprgroup RPAREN LBRACKET S RBRACKET','ifcommand',7,'p_if','parser.py',89),
  ('ifcommand -> IF LPAREN relexprgroup RPAREN LBRACKET S RBRACKET ELSE ifcommand','ifcommand',9,'p_if','parser.py',90),
  ('ifcommand -> IF LPAREN relexprgroup RPAREN LBRACKET S RBRACKET ELSE LBRACKET S RBRACKET','ifcommand',11,'p_if','parser.py',91),
  ('expr -> expr PLUS expr','expr',3,'p_binary_expression','parser.py',103),
  ('expr -> expr MINUS expr','expr',3,'p_binary_expression','parser.py',104),
  ('expr -> expr TIMES expr','expr',3,'p_binary_expression','parser.py',105),
  ('expr -> expr DIVIDE expr','expr',3,'p_binary_expression','parser.py',106),
  ('expr -> expr MOD expr','expr',3,'p_binary_expression','parser.py',107),
  ('expr -> expr INCREMENT','expr',2,'p_unary_expressions','parser.py',115),
  ('expr -> expr DECREMENT','expr',2,'p_unary_expressions','parser.py',116),
  ('expr -> ID ASSIGN expr','expr',3,'p_assign_expression','parser.py',121),
  ('expr -> NUMBER','expr',1,'p_number_expression','parser.py',126),
  ('expr -> STRINGS','expr',1,'p_string_expression','parser.py',131),
  ('expr -> ID','expr',1,'p_variable_expression','parser.py',136),
  ('expr -> LPAREN expr RPAREN','expr',3,'p_group_expression','parser.py',141),
  ('relexpr -> expr LT expr','relexpr',3,'p_relational_expressions','parser.py',150),
  ('relexpr -> expr LE expr','relexpr',3,'p_relational_expressions','parser.py',151),
  ('relexpr -> expr GT expr','relexpr',3,'p_relational_expressions','parser.py',152),
  ('relexpr -> expr GE expr','relexpr',3,'p_relational_expressions','parser.py',153),
  ('relexpr -> expr EQUALS expr','relexpr',3,'p_relational_expressions','parser.py',154),
  ('relexpr -> expr NE expr','relexpr',3,'p_relational_expressions','parser.py',155),
  ('relexprgroup -> relexpr AND relexprgroup','relexprgroup',3,'p_rel_group','parser.py',160),
  ('relexprgroup -> relexpr OR relexprgroup','relexprgroup',3,'p_rel_group','parser.py',161),
  ('relexprgroup -> relexpr','relexprgroup',1,'p_rel_group','parser.py',162),
]
