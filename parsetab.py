
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.8'

_lr_method = 'LALR'

_lr_signature = 'EC69DF328EE63B93322B0BD80F3BD7F0'
    
_lr_action_items = {'AND':([3,5,6,15,16,17,18,],[-1,-2,7,-3,-6,-5,-4,]),'RPAREN':([3,5,11,12,13,14,15,16,17,18,],[-1,-2,15,16,17,18,-3,-6,-5,-4,]),'ARROW':([3,5,6,15,16,17,18,],[-1,-2,9,-3,-6,-5,-4,]),'NEG':([0,2,4,7,8,9,10,],[2,2,2,2,2,2,2,]),'IFF':([3,5,6,15,16,17,18,],[-1,-2,8,-3,-6,-5,-4,]),'PROP_VAR':([0,2,4,7,8,9,10,],[3,3,3,3,3,3,3,]),'LPAREN':([0,2,4,7,8,9,10,],[4,4,4,4,4,4,4,]),'OR':([3,5,6,15,16,17,18,],[-1,-2,10,-3,-6,-5,-4,]),'$end':([1,3,5,15,16,17,18,],[0,-1,-2,-3,-6,-5,-4,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'compound_prop':([0,2,4,7,8,9,10,],[1,5,6,11,12,13,14,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> compound_prop","S'",1,None,None,None),
  ('compound_prop -> PROP_VAR','compound_prop',1,'p_compound_prop_PROP_VAR','tree_yacc.py',25),
  ('compound_prop -> NEG compound_prop','compound_prop',2,'p_compound_prop_NEG','tree_yacc.py',29),
  ('compound_prop -> LPAREN compound_prop AND compound_prop RPAREN','compound_prop',5,'p_compound_prop_AND','tree_yacc.py',33),
  ('compound_prop -> LPAREN compound_prop OR compound_prop RPAREN','compound_prop',5,'p_compound_prop_OR','tree_yacc.py',37),
  ('compound_prop -> LPAREN compound_prop ARROW compound_prop RPAREN','compound_prop',5,'p_compound_prop_ARROW','tree_yacc.py',41),
  ('compound_prop -> LPAREN compound_prop IFF compound_prop RPAREN','compound_prop',5,'p_compound_prop_IFF','tree_yacc.py',45),
]