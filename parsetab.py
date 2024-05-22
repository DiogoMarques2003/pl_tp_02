
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "left+-left*/rightUMINUSCOMENTARIO CONCAT ENTRADA ESCREVER FIM FIMSE FOLD FUNCAO MAP NEG NUM SE SENAO STRING VAR_IDlista_declaracoes : declaracao\n                             | lista_declaracoes declaracaodeclaracao : declaracao_atribuicao\n                      | declaracao_expressao\n                      | declaracao_funcao\n                      | declaracao_se\n                      | declaracao_escrever\n                      | declaracao_comentariodeclaracao_atribuicao : VAR_ID '=' lista_expressoes ';'declaracao_atribuicao : atribuicao\n                                 | declaracao_atribuicao ',' atribuicao ';'atribuicao : VAR_ID '=' expressaolista_variaveis : lista_variaveis ',' VAR_ID\n                           | VAR_IDlista_expressoes : lista_expressoes ',' expressao\n                            | expressaodeclaracao_expressao : expressao ';'expressao : expressao '+' expressao\n                     | expressao '-' expressao\n                     | expressao '*' expressao\n                     | expressao '/' expressaoexpressao : '(' expressao ')'expressao : '-' expressao %prec UMINUSexpressao : NUMexpressao : STRINGexpressao : VAR_IDexpressao : VAR_ID '[' ']'expressao : '[' lista_elementos  ']' declaracao_atribuicao : VAR_ID '[' ']' '=' '[' lista_elementos ']' ';'lista_elementos : lista_elementos ',' expressao\n                           | expressao\n                           | vazioexpressao : MAP '(' VAR_ID ',' lista_expressoes ')'expressao : FOLD '(' VAR_ID ',' lista_expressoes ',' expressao ')'expressao : VAR_ID '(' lista_expressoes ')'declaracao_funcao : FUNCAO VAR_ID '(' lista_parametros_opcional ')' ':' bloco_funcao FIM\n                             | FUNCAO VAR_ID '(' lista_parametros_opcional ')' ',' ':' expressao ';'lista_parametros_opcional : lista_parametros\n                                     | vaziolista_parametros : lista_parametros ',' VAR_ID\n                            | lista_parametros ',' NUM\n                            | lista_parametros ',' array_vazio\n                            | lista_parametros ',' var_array\n                            | VAR_ID\n                            | NUM\n                            | array_vazio\n                            | var_arrayarray_vazio : '[' ']'var_array : VAR_ID ':' VAR_ID '[' ']' declaracao_se : SE expressao ':' lista_declaracoes senao_opcional FIMsenao_opcional : SENAO ':' lista_declaracoes\n                          | vaziodeclaracao_escrever : ESCREVER '(' expressao ')' ';'declaracao_comentario : COMENTARIOvazio :expressao : expressao CONCAT expressaobloco_funcao : lista_declaracoes"
    
_lr_action_items = {'VAR_ID':([0,1,2,3,4,5,6,7,8,10,11,13,14,15,17,18,19,20,23,24,25,27,31,32,33,34,35,36,37,41,42,43,44,48,52,53,55,56,57,58,59,60,61,62,66,67,68,69,71,73,82,84,85,88,89,91,96,101,107,108,109,110,114,115,116,118,120,122,123,],[9,9,-1,-3,-4,-5,-6,-7,-8,-10,31,38,31,31,-54,31,-24,-25,-2,46,31,31,-26,-17,31,31,31,31,31,31,-23,64,65,-12,-28,31,-18,-19,-20,-21,-56,74,-22,9,-11,31,-9,31,-35,-27,9,31,31,31,100,103,-53,9,-50,9,-33,31,9,31,9,-29,-36,-34,-37,]),'FUNCAO':([0,1,2,3,4,5,6,7,8,10,17,19,20,23,31,32,42,48,52,55,56,57,58,59,61,62,66,68,71,73,82,96,101,107,108,109,114,116,118,120,122,123,],[13,13,-1,-3,-4,-5,-6,-7,-8,-10,-54,-24,-25,-2,-26,-17,-23,-12,-28,-18,-19,-20,-21,-56,-22,13,-11,-9,-35,-27,13,-53,13,-50,13,-33,13,13,-29,-36,-34,-37,]),'SE':([0,1,2,3,4,5,6,7,8,10,17,19,20,23,31,32,42,48,52,55,56,57,58,59,61,62,66,68,71,73,82,96,101,107,108,109,114,116,118,120,122,123,],[15,15,-1,-3,-4,-5,-6,-7,-8,-10,-54,-24,-25,-2,-26,-17,-23,-12,-28,-18,-19,-20,-21,-56,-22,15,-11,-9,-35,-27,15,-53,15,-50,15,-33,15,15,-29,-36,-34,-37,]),'ESCREVER':([0,1,2,3,4,5,6,7,8,10,17,19,20,23,31,32,42,48,52,55,56,57,58,59,61,62,66,68,71,73,82,96,101,107,108,109,114,116,118,120,122,123,],[16,16,-1,-3,-4,-5,-6,-7,-8,-10,-54,-24,-25,-2,-26,-17,-23,-12,-28,-18,-19,-20,-21,-56,-22,16,-11,-9,-35,-27,16,-53,16,-50,16,-33,16,16,-29,-36,-34,-37,]),'COMENTARIO':([0,1,2,3,4,5,6,7,8,10,17,19,20,23,31,32,42,48,52,55,56,57,58,59,61,62,66,68,71,73,82,96,101,107,108,109,114,116,118,120,122,123,],[17,17,-1,-3,-4,-5,-6,-7,-8,-10,-54,-24,-25,-2,-26,-17,-23,-12,-28,-18,-19,-20,-21,-56,-22,17,-11,-9,-35,-27,17,-53,17,-50,17,-33,17,17,-29,-36,-34,-37,]),'(':([0,1,2,3,4,5,6,7,8,9,10,11,14,15,16,17,18,19,20,21,22,23,25,27,31,32,33,34,35,36,37,38,41,42,48,52,53,55,56,57,58,59,61,62,66,67,68,69,71,73,82,84,85,88,96,101,107,108,109,110,114,115,116,118,120,122,123,],[14,14,-1,-3,-4,-5,-6,-7,-8,27,-10,14,14,14,41,-54,14,-24,-25,43,44,-2,14,14,27,-17,14,14,14,14,14,60,14,-23,-12,-28,14,-18,-19,-20,-21,-56,-22,14,-11,14,-9,14,-35,-27,14,14,14,14,-53,14,-50,14,-33,14,14,14,14,-29,-36,-34,-37,]),'-':([0,1,2,3,4,5,6,7,8,9,10,11,12,14,15,17,18,19,20,23,25,27,29,31,32,33,34,35,36,37,39,40,41,42,48,49,51,52,53,55,56,57,58,59,61,62,63,66,67,68,69,71,72,73,82,84,85,86,87,88,96,101,107,108,109,110,114,115,116,117,118,120,121,122,123,],[18,18,-1,-3,-4,-5,-6,-7,-8,-26,-10,18,34,18,18,-54,18,-24,-25,-2,18,18,34,-26,-17,18,18,18,18,18,34,34,18,-23,34,-27,34,-28,18,-18,-19,-20,-21,34,-22,18,34,-11,18,-9,18,-35,34,-27,18,18,18,34,34,18,-53,18,-50,18,-33,18,18,18,18,34,-29,-36,34,-34,-37,]),'NUM':([0,1,2,3,4,5,6,7,8,10,11,14,15,17,18,19,20,23,25,27,31,32,33,34,35,36,37,41,42,48,52,53,55,56,57,58,59,60,61,62,66,67,68,69,71,73,82,84,85,88,91,96,101,107,108,109,110,114,115,116,118,120,122,123,],[19,19,-1,-3,-4,-5,-6,-7,-8,-10,19,19,19,-54,19,-24,-25,-2,19,19,-26,-17,19,19,19,19,19,19,-23,-12,-28,19,-18,-19,-20,-21,-56,78,-22,19,-11,19,-9,19,-35,-27,19,19,19,19,104,-53,19,-50,19,-33,19,19,19,19,-29,-36,-34,-37,]),'STRING':([0,1,2,3,4,5,6,7,8,10,11,14,15,17,18,19,20,23,25,27,31,32,33,34,35,36,37,41,42,48,52,53,55,56,57,58,59,61,62,66,67,68,69,71,73,82,84,85,88,96,101,107,108,109,110,114,115,116,118,120,122,123,],[20,20,-1,-3,-4,-5,-6,-7,-8,-10,20,20,20,-54,20,-24,-25,-2,20,20,-26,-17,20,20,20,20,20,20,-23,-12,-28,20,-18,-19,-20,-21,-56,-22,20,-11,20,-9,20,-35,-27,20,20,20,20,-53,20,-50,20,-33,20,20,20,20,-29,-36,-34,-37,]),'[':([0,1,2,3,4,5,6,7,8,9,10,11,14,15,17,18,19,20,23,25,27,31,32,33,34,35,36,37,41,42,48,52,53,55,56,57,58,59,60,61,62,66,67,68,69,70,71,73,82,84,85,88,91,96,100,101,107,108,109,110,114,115,116,118,120,122,123,],[11,11,-1,-3,-4,-5,-6,-7,-8,26,-10,11,11,11,-54,11,-24,-25,-2,11,11,54,-17,11,11,11,11,11,11,-23,-12,-28,11,-18,-19,-20,-21,-56,81,-22,11,-11,11,-9,11,88,-35,-27,11,11,11,11,81,-53,112,11,-50,11,-33,11,11,11,11,-29,-36,-34,-37,]),'MAP':([0,1,2,3,4,5,6,7,8,10,11,14,15,17,18,19,20,23,25,27,31,32,33,34,35,36,37,41,42,48,52,53,55,56,57,58,59,61,62,66,67,68,69,71,73,82,84,85,88,96,101,107,108,109,110,114,115,116,118,120,122,123,],[21,21,-1,-3,-4,-5,-6,-7,-8,-10,21,21,21,-54,21,-24,-25,-2,21,21,-26,-17,21,21,21,21,21,21,-23,-12,-28,21,-18,-19,-20,-21,-56,-22,21,-11,21,-9,21,-35,-27,21,21,21,21,-53,21,-50,21,-33,21,21,21,21,-29,-36,-34,-37,]),'FOLD':([0,1,2,3,4,5,6,7,8,10,11,14,15,17,18,19,20,23,25,27,31,32,33,34,35,36,37,41,42,48,52,53,55,56,57,58,59,61,62,66,67,68,69,71,73,82,84,85,88,96,101,107,108,109,110,114,115,116,118,120,122,123,],[22,22,-1,-3,-4,-5,-6,-7,-8,-10,22,22,22,-54,22,-24,-25,-2,22,22,-26,-17,22,22,22,22,22,22,-23,-12,-28,22,-18,-19,-20,-21,-56,-22,22,-11,22,-9,22,-35,-27,22,22,22,22,-53,22,-50,22,-33,22,22,22,22,-29,-36,-34,-37,]),'$end':([1,2,3,4,5,6,7,8,10,17,19,20,23,31,32,42,48,52,55,56,57,58,59,61,66,68,71,73,96,107,109,118,120,122,123,],[0,-1,-3,-4,-5,-6,-7,-8,-10,-54,-24,-25,-2,-26,-17,-23,-12,-28,-18,-19,-20,-21,-56,-22,-11,-9,-35,-27,-53,-50,-33,-29,-36,-34,-37,]),'SENAO':([2,3,4,5,6,7,8,10,17,19,20,23,31,32,42,48,52,55,56,57,58,59,61,66,68,71,73,82,96,107,109,118,120,122,123,],[-1,-3,-4,-5,-6,-7,-8,-10,-54,-24,-25,-2,-26,-17,-23,-12,-28,-18,-19,-20,-21,-56,-22,-11,-9,-35,-27,94,-53,-50,-33,-29,-36,-34,-37,]),'FIM':([2,3,4,5,6,7,8,10,17,19,20,23,31,32,42,48,52,55,56,57,58,59,61,66,68,71,73,82,93,95,96,107,109,113,114,116,118,120,122,123,],[-1,-3,-4,-5,-6,-7,-8,-10,-54,-24,-25,-2,-26,-17,-23,-12,-28,-18,-19,-20,-21,-56,-22,-11,-9,-35,-27,-55,107,-52,-53,-50,-33,120,-57,-51,-29,-36,-34,-37,]),',':([3,10,11,19,20,28,29,30,31,42,47,48,50,51,52,55,56,57,58,59,61,64,65,66,68,71,72,73,74,76,78,79,80,87,88,90,92,97,98,99,103,104,105,106,109,117,118,119,122,],[24,-10,-55,-24,-25,53,-31,-32,-26,-23,69,-12,69,-16,-28,-18,-19,-20,-21,-56,-22,84,85,-11,-9,-35,-30,-27,-44,91,-45,-46,-47,-15,-55,102,-48,69,110,53,-40,-41,-42,-43,-33,-15,-29,-49,-34,]),'=':([9,46,49,],[25,67,70,]),';':([9,12,19,20,31,42,45,47,48,49,52,55,56,57,58,59,61,71,73,83,86,87,109,111,121,122,],[-26,32,-24,-25,-26,-23,66,68,-16,-27,-28,-18,-19,-20,-21,-56,-22,-35,-27,96,-12,-15,-33,118,123,-34,]),'+':([9,12,19,20,29,31,39,40,42,48,49,51,52,55,56,57,58,59,61,63,71,72,73,86,87,109,117,121,122,],[-26,33,-24,-25,33,-26,33,33,-23,33,-27,33,-28,-18,-19,-20,-21,33,-22,33,-35,33,-27,33,33,-33,33,33,-34,]),'*':([9,12,19,20,29,31,39,40,42,48,49,51,52,55,56,57,58,59,61,63,71,72,73,86,87,109,117,121,122,],[-26,35,-24,-25,35,-26,35,35,-23,35,-27,35,-28,35,35,-20,-21,35,-22,35,-35,35,-27,35,35,-33,35,35,-34,]),'/':([9,12,19,20,29,31,39,40,42,48,49,51,52,55,56,57,58,59,61,63,71,72,73,86,87,109,117,121,122,],[-26,36,-24,-25,36,-26,36,36,-23,36,-27,36,-28,36,36,-20,-21,36,-22,36,-35,36,-27,36,36,-33,36,36,-34,]),'CONCAT':([9,12,19,20,29,31,39,40,42,48,49,51,52,55,56,57,58,59,61,63,71,72,73,86,87,109,117,121,122,],[-26,37,-24,-25,37,-26,37,37,-23,37,-27,37,-28,-18,-19,-20,-21,37,-22,37,-35,37,-27,37,37,-33,37,37,-34,]),']':([11,19,20,26,28,29,30,31,42,52,54,55,56,57,58,59,61,71,72,73,81,88,99,109,112,122,],[-55,-24,-25,49,52,-31,-32,-26,-23,-28,73,-18,-19,-20,-21,-56,-22,-35,-30,-27,92,-55,111,-33,119,-34,]),')':([19,20,31,39,42,50,51,52,55,56,57,58,59,60,61,63,71,73,74,75,76,77,78,79,80,87,92,97,103,104,105,106,109,117,119,122,],[-24,-25,-26,61,-23,71,-16,-28,-18,-19,-20,-21,-56,-55,-22,83,-35,-27,-44,90,-38,-39,-45,-46,-47,-15,-48,109,-40,-41,-42,-43,-33,122,-49,-34,]),':':([19,20,31,40,42,52,55,56,57,58,59,61,71,73,74,90,94,102,103,109,122,],[-24,-25,-26,62,-23,-28,-18,-19,-20,-21,-56,-22,-35,-27,89,101,108,115,89,-33,-34,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'lista_declaracoes':([0,62,101,108,],[1,82,114,116,]),'declaracao':([0,1,62,82,101,108,114,116,],[2,23,2,23,2,2,23,23,]),'declaracao_atribuicao':([0,1,62,82,101,108,114,116,],[3,3,3,3,3,3,3,3,]),'declaracao_expressao':([0,1,62,82,101,108,114,116,],[4,4,4,4,4,4,4,4,]),'declaracao_funcao':([0,1,62,82,101,108,114,116,],[5,5,5,5,5,5,5,5,]),'declaracao_se':([0,1,62,82,101,108,114,116,],[6,6,6,6,6,6,6,6,]),'declaracao_escrever':([0,1,62,82,101,108,114,116,],[7,7,7,7,7,7,7,7,]),'declaracao_comentario':([0,1,62,82,101,108,114,116,],[8,8,8,8,8,8,8,8,]),'atribuicao':([0,1,24,62,82,101,108,114,116,],[10,10,45,10,10,10,10,10,10,]),'expressao':([0,1,11,14,15,18,25,27,33,34,35,36,37,41,53,62,67,69,82,84,85,88,101,108,110,114,115,116,],[12,12,29,39,40,42,48,51,55,56,57,58,59,63,72,12,86,87,12,51,51,29,12,12,117,12,121,12,]),'lista_elementos':([11,88,],[28,99,]),'vazio':([11,60,82,88,],[30,77,95,30,]),'lista_expressoes':([25,27,84,85,],[47,50,97,98,]),'lista_parametros_opcional':([60,],[75,]),'lista_parametros':([60,],[76,]),'array_vazio':([60,91,],[79,105,]),'var_array':([60,91,],[80,106,]),'senao_opcional':([82,],[93,]),'bloco_funcao':([101,],[113,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> lista_declaracoes","S'",1,None,None,None),
  ('lista_declaracoes -> declaracao','lista_declaracoes',1,'p_lista_declaracoes','arith_grammar.py',37),
  ('lista_declaracoes -> lista_declaracoes declaracao','lista_declaracoes',2,'p_lista_declaracoes','arith_grammar.py',38),
  ('declaracao -> declaracao_atribuicao','declaracao',1,'p_declaracao','arith_grammar.py',47),
  ('declaracao -> declaracao_expressao','declaracao',1,'p_declaracao','arith_grammar.py',48),
  ('declaracao -> declaracao_funcao','declaracao',1,'p_declaracao','arith_grammar.py',49),
  ('declaracao -> declaracao_se','declaracao',1,'p_declaracao','arith_grammar.py',50),
  ('declaracao -> declaracao_escrever','declaracao',1,'p_declaracao','arith_grammar.py',51),
  ('declaracao -> declaracao_comentario','declaracao',1,'p_declaracao','arith_grammar.py',52),
  ('declaracao_atribuicao -> VAR_ID = lista_expressoes ;','declaracao_atribuicao',4,'p_declaracao_atribuicao','arith_grammar.py',57),
  ('declaracao_atribuicao -> atribuicao','declaracao_atribuicao',1,'p_declaracao_atribuicao_multipla','arith_grammar.py',64),
  ('declaracao_atribuicao -> declaracao_atribuicao , atribuicao ;','declaracao_atribuicao',4,'p_declaracao_atribuicao_multipla','arith_grammar.py',65),
  ('atribuicao -> VAR_ID = expressao','atribuicao',3,'p_atribuicao','arith_grammar.py',79),
  ('lista_variaveis -> lista_variaveis , VAR_ID','lista_variaveis',3,'p_lista_variaveis','arith_grammar.py',83),
  ('lista_variaveis -> VAR_ID','lista_variaveis',1,'p_lista_variaveis','arith_grammar.py',84),
  ('lista_expressoes -> lista_expressoes , expressao','lista_expressoes',3,'p_lista_expressoes','arith_grammar.py',92),
  ('lista_expressoes -> expressao','lista_expressoes',1,'p_lista_expressoes','arith_grammar.py',93),
  ('declaracao_expressao -> expressao ;','declaracao_expressao',2,'p_declaracao_expressao','arith_grammar.py',104),
  ('expressao -> expressao + expressao','expressao',3,'p_expressao','arith_grammar.py',109),
  ('expressao -> expressao - expressao','expressao',3,'p_expressao','arith_grammar.py',110),
  ('expressao -> expressao * expressao','expressao',3,'p_expressao','arith_grammar.py',111),
  ('expressao -> expressao / expressao','expressao',3,'p_expressao','arith_grammar.py',112),
  ('expressao -> ( expressao )','expressao',3,'p_expressao_grupo','arith_grammar.py',117),
  ('expressao -> - expressao','expressao',2,'p_expressao_uminus','arith_grammar.py',122),
  ('expressao -> NUM','expressao',1,'p_expressao_num','arith_grammar.py',127),
  ('expressao -> STRING','expressao',1,'p_expressao_string','arith_grammar.py',132),
  ('expressao -> VAR_ID','expressao',1,'p_expressao_var_id','arith_grammar.py',153),
  ('expressao -> VAR_ID [ ]','expressao',3,'p_expressao_var_array','arith_grammar.py',158),
  ('expressao -> [ lista_elementos ]','expressao',3,'p_expressao_array','arith_grammar.py',163),
  ('declaracao_atribuicao -> VAR_ID [ ] = [ lista_elementos ] ;','declaracao_atribuicao',8,'p_expressao_array_init','arith_grammar.py',168),
  ('lista_elementos -> lista_elementos , expressao','lista_elementos',3,'p_lista_elementos','arith_grammar.py',173),
  ('lista_elementos -> expressao','lista_elementos',1,'p_lista_elementos','arith_grammar.py',174),
  ('lista_elementos -> vazio','lista_elementos',1,'p_lista_elementos','arith_grammar.py',175),
  ('expressao -> MAP ( VAR_ID , lista_expressoes )','expressao',6,'p_expressao_map','arith_grammar.py',187),
  ('expressao -> FOLD ( VAR_ID , lista_expressoes , expressao )','expressao',8,'p_expressao_fold','arith_grammar.py',192),
  ('expressao -> VAR_ID ( lista_expressoes )','expressao',4,'p_expressao_chamada_funcao','arith_grammar.py',197),
  ('declaracao_funcao -> FUNCAO VAR_ID ( lista_parametros_opcional ) : bloco_funcao FIM','declaracao_funcao',8,'p_declaracao_funcao','arith_grammar.py',205),
  ('declaracao_funcao -> FUNCAO VAR_ID ( lista_parametros_opcional ) , : expressao ;','declaracao_funcao',9,'p_declaracao_funcao','arith_grammar.py',206),
  ('lista_parametros_opcional -> lista_parametros','lista_parametros_opcional',1,'p_lista_parametros_opcional','arith_grammar.py',215),
  ('lista_parametros_opcional -> vazio','lista_parametros_opcional',1,'p_lista_parametros_opcional','arith_grammar.py',216),
  ('lista_parametros -> lista_parametros , VAR_ID','lista_parametros',3,'p_lista_parametros','arith_grammar.py',221),
  ('lista_parametros -> lista_parametros , NUM','lista_parametros',3,'p_lista_parametros','arith_grammar.py',222),
  ('lista_parametros -> lista_parametros , array_vazio','lista_parametros',3,'p_lista_parametros','arith_grammar.py',223),
  ('lista_parametros -> lista_parametros , var_array','lista_parametros',3,'p_lista_parametros','arith_grammar.py',224),
  ('lista_parametros -> VAR_ID','lista_parametros',1,'p_lista_parametros','arith_grammar.py',225),
  ('lista_parametros -> NUM','lista_parametros',1,'p_lista_parametros','arith_grammar.py',226),
  ('lista_parametros -> array_vazio','lista_parametros',1,'p_lista_parametros','arith_grammar.py',227),
  ('lista_parametros -> var_array','lista_parametros',1,'p_lista_parametros','arith_grammar.py',228),
  ('array_vazio -> [ ]','array_vazio',2,'p_empty_list','arith_grammar.py',237),
  ('var_array -> VAR_ID : VAR_ID [ ]','var_array',5,'p_var_array','arith_grammar.py',242),
  ('declaracao_se -> SE expressao : lista_declaracoes senao_opcional FIM','declaracao_se',6,'p_declaracao_se','arith_grammar.py',248),
  ('senao_opcional -> SENAO : lista_declaracoes','senao_opcional',3,'p_senao_opcional','arith_grammar.py',253),
  ('senao_opcional -> vazio','senao_opcional',1,'p_senao_opcional','arith_grammar.py',254),
  ('declaracao_escrever -> ESCREVER ( expressao ) ;','declaracao_escrever',5,'p_declaracao_escrever','arith_grammar.py',259),
  ('declaracao_comentario -> COMENTARIO','declaracao_comentario',1,'p_declaracao_comentario','arith_grammar.py',264),
  ('vazio -> <empty>','vazio',0,'p_vazio','arith_grammar.py',269),
  ('expressao -> expressao CONCAT expressao','expressao',3,'p_expressao_concat','arith_grammar.py',274),
  ('bloco_funcao -> lista_declaracoes','bloco_funcao',1,'p_bloco_funcao','arith_grammar.py',279),
]
