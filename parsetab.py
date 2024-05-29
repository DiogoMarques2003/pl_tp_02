
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "left+-left*/rightUMINUSUNARY_NEGALEATORIO COMENTARIO CONCAT ENTRADA ESCREVER FIM FOLD FUNCAO MAP NEG NUM SE SENAO SENAOSE STRING VAR_IDlista_declaracoes : declaracao\n                             | lista_declaracoes declaracaodeclaracao : declaracao_atribuicao\n                      | declaracao_expressao\n                      | declaracao_funcao\n                      | declaracao_se\n                      | declaracao_escrever\n                      | declaracao_comentariodeclaracao_atribuicao : VAR_ID '=' lista_expressoes ';'declaracao_atribuicao : atribuicao\n                                 | declaracao_atribuicao ',' atribuicao ';'atribuicao : VAR_ID '=' expressaolista_expressoes : lista_expressoes ',' expressao\n                            | expressaodeclaracao_expressao : expressao ';'expressao : expressao '+' expressao\n                     | expressao '-' expressao\n                     | expressao '*' expressao\n                     | expressao '/' expressao\n                     | expressao '=' '=' expressao\n                     | expressao '<' expressao\n                     | expressao '>' expressao\n                     | expressao '<' '=' expressao\n                     | expressao '>' '=' expressao\n                     | expressao '!' '=' expressaoexpressao : '(' expressao ')'expressao : '-' expressao %prec UMINUSexpressao : NUMexpressao : STRINGexpressao : VAR_IDexpressao : VAR_ID '[' ']'expressao : '[' lista_elementos  ']' declaracao_atribuicao : VAR_ID '[' ']' '=' '[' lista_elementos ']' ';'lista_elementos : lista_elementos ',' expressao\n                           | expressao\n                           | vazioexpressao : MAP '(' VAR_ID ',' lista_expressoes ')'expressao : FOLD '(' VAR_ID ',' lista_expressoes ',' expressao ')'expressao : ENTRADA '(' ')'expressao : ALEATORIO '(' NUM ')'expressao : VAR_ID '(' lista_expressoes ')'declaracao_funcao : FUNCAO VAR_ID '(' lista_parametros_opcional ')' ':' bloco_funcao FIM\n                             | FUNCAO VAR_ID '(' lista_parametros_opcional ')' ',' ':' expressao ';'lista_parametros_opcional : lista_parametros\n                                     | vaziolista_parametros : lista_parametros ',' expressao\n                            | lista_parametros ',' var_id_array\n                            | expressao\n                            | var_id_arrayexpressao : '[' ']'var_id_array : VAR_ID ':' VAR_ID '[' ']' declaracao_se : SE expressao ':' lista_declaracoes senao FIMsenao : SENAO ':' lista_declaracoes\n                 | SENAOSE expressao ':' lista_declaracoes\n                 | vazioexpressao : NEG expressao %prec UNARY_NEGdeclaracao_escrever : ESCREVER '(' expressao ')' ';'declaracao_comentario : COMENTARIOvazio :expressao : expressao CONCAT expressaobloco_funcao : lista_declaracoes"
    
_lr_action_items = {'VAR_ID':([0,1,2,3,4,5,6,7,8,10,11,13,14,15,17,18,19,20,25,26,27,28,30,32,35,36,37,38,39,40,42,43,45,49,50,51,52,55,59,63,64,66,67,68,69,70,71,72,73,74,75,76,77,78,79,83,85,86,87,88,90,92,93,94,95,96,103,105,106,107,110,111,113,116,118,123,127,128,130,131,135,136,137,138,140,142,144,145,146,],[9,9,-1,-3,-4,-5,-6,-7,-8,-10,35,46,35,35,-58,35,-28,-29,35,-2,57,35,35,-50,-30,-15,35,35,35,35,35,35,35,35,-27,81,82,-56,-12,-32,35,-16,-17,-18,-19,35,-21,35,-22,35,35,-60,97,-26,9,-39,-11,35,-9,35,-41,-31,-20,-23,-24,-25,9,35,35,-40,35,122,97,35,-57,9,-52,9,-37,35,9,35,9,9,-33,-42,9,-38,-43,]),'FUNCAO':([0,1,2,3,4,5,6,7,8,10,17,19,20,26,32,35,36,50,55,59,63,66,67,68,69,71,73,76,78,79,83,85,87,90,92,93,94,95,96,103,107,118,123,127,128,130,135,137,138,140,142,144,145,146,],[13,13,-1,-3,-4,-5,-6,-7,-8,-10,-58,-28,-29,-2,-50,-30,-15,-27,-56,-12,-32,-16,-17,-18,-19,-21,-22,-60,-26,13,-39,-11,-9,-41,-31,-20,-23,-24,-25,13,-40,-57,13,-52,13,-37,13,13,13,-33,-42,13,-38,-43,]),'SE':([0,1,2,3,4,5,6,7,8,10,17,19,20,26,32,35,36,50,55,59,63,66,67,68,69,71,73,76,78,79,83,85,87,90,92,93,94,95,96,103,107,118,123,127,128,130,135,137,138,140,142,144,145,146,],[15,15,-1,-3,-4,-5,-6,-7,-8,-10,-58,-28,-29,-2,-50,-30,-15,-27,-56,-12,-32,-16,-17,-18,-19,-21,-22,-60,-26,15,-39,-11,-9,-41,-31,-20,-23,-24,-25,15,-40,-57,15,-52,15,-37,15,15,15,-33,-42,15,-38,-43,]),'ESCREVER':([0,1,2,3,4,5,6,7,8,10,17,19,20,26,32,35,36,50,55,59,63,66,67,68,69,71,73,76,78,79,83,85,87,90,92,93,94,95,96,103,107,118,123,127,128,130,135,137,138,140,142,144,145,146,],[16,16,-1,-3,-4,-5,-6,-7,-8,-10,-58,-28,-29,-2,-50,-30,-15,-27,-56,-12,-32,-16,-17,-18,-19,-21,-22,-60,-26,16,-39,-11,-9,-41,-31,-20,-23,-24,-25,16,-40,-57,16,-52,16,-37,16,16,16,-33,-42,16,-38,-43,]),'COMENTARIO':([0,1,2,3,4,5,6,7,8,10,17,19,20,26,32,35,36,50,55,59,63,66,67,68,69,71,73,76,78,79,83,85,87,90,92,93,94,95,96,103,107,118,123,127,128,130,135,137,138,140,142,144,145,146,],[17,17,-1,-3,-4,-5,-6,-7,-8,-10,-58,-28,-29,-2,-50,-30,-15,-27,-56,-12,-32,-16,-17,-18,-19,-21,-22,-60,-26,17,-39,-11,-9,-41,-31,-20,-23,-24,-25,17,-40,-57,17,-52,17,-37,17,17,17,-33,-42,17,-38,-43,]),'(':([0,1,2,3,4,5,6,7,8,9,10,11,14,15,16,17,18,19,20,21,22,23,24,25,26,28,30,32,35,36,37,38,39,40,42,43,45,46,49,50,55,59,63,64,66,67,68,69,70,71,72,73,74,75,76,77,78,79,83,85,86,87,88,90,92,93,94,95,96,97,103,105,106,107,110,113,116,118,123,127,128,130,131,135,136,137,138,140,142,144,145,146,],[14,14,-1,-3,-4,-5,-6,-7,-8,30,-10,14,14,14,49,-58,14,-28,-29,51,52,53,54,14,-2,14,14,-50,30,-15,14,14,14,14,14,14,14,77,14,-27,-56,-12,-32,14,-16,-17,-18,-19,14,-21,14,-22,14,14,-60,14,-26,14,-39,-11,14,-9,14,-41,-31,-20,-23,-24,-25,30,14,14,14,-40,14,14,14,-57,14,-52,14,-37,14,14,14,14,14,-33,-42,14,-38,-43,]),'-':([0,1,2,3,4,5,6,7,8,9,10,11,12,14,15,17,18,19,20,25,26,28,30,32,33,35,36,37,38,39,40,42,43,45,47,48,49,50,55,59,60,62,63,64,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,83,85,86,87,88,90,91,92,93,94,95,96,97,99,103,105,106,107,108,109,110,113,116,118,123,125,127,128,129,130,131,135,136,137,138,139,140,142,143,144,145,146,],[18,18,-1,-3,-4,-5,-6,-7,-8,-30,-10,18,38,18,18,-58,18,-28,-29,18,-2,18,18,-50,38,-30,-15,18,18,18,18,18,18,18,38,38,18,-27,-56,38,-31,38,-32,18,-16,-17,-18,-19,18,38,18,38,18,18,38,18,-26,18,38,-39,-11,18,-9,18,-41,38,-31,38,38,38,38,-30,38,18,18,18,-40,38,38,18,18,18,-57,18,38,-52,18,38,-37,18,18,18,18,18,38,-33,-42,38,18,-38,-43,]),'NUM':([0,1,2,3,4,5,6,7,8,10,11,14,15,17,18,19,20,25,26,28,30,32,35,36,37,38,39,40,42,43,45,49,50,54,55,59,63,64,66,67,68,69,70,71,72,73,74,75,76,77,78,79,83,85,86,87,88,90,92,93,94,95,96,103,105,106,107,110,113,116,118,123,127,128,130,131,135,136,137,138,140,142,144,145,146,],[19,19,-1,-3,-4,-5,-6,-7,-8,-10,19,19,19,-58,19,-28,-29,19,-2,19,19,-50,-30,-15,19,19,19,19,19,19,19,19,-27,84,-56,-12,-32,19,-16,-17,-18,-19,19,-21,19,-22,19,19,-60,19,-26,19,-39,-11,19,-9,19,-41,-31,-20,-23,-24,-25,19,19,19,-40,19,19,19,-57,19,-52,19,-37,19,19,19,19,19,-33,-42,19,-38,-43,]),'STRING':([0,1,2,3,4,5,6,7,8,10,11,14,15,17,18,19,20,25,26,28,30,32,35,36,37,38,39,40,42,43,45,49,50,55,59,63,64,66,67,68,69,70,71,72,73,74,75,76,77,78,79,83,85,86,87,88,90,92,93,94,95,96,103,105,106,107,110,113,116,118,123,127,128,130,131,135,136,137,138,140,142,144,145,146,],[20,20,-1,-3,-4,-5,-6,-7,-8,-10,20,20,20,-58,20,-28,-29,20,-2,20,20,-50,-30,-15,20,20,20,20,20,20,20,20,-27,-56,-12,-32,20,-16,-17,-18,-19,20,-21,20,-22,20,20,-60,20,-26,20,-39,-11,20,-9,20,-41,-31,-20,-23,-24,-25,20,20,20,-40,20,20,20,-57,20,-52,20,-37,20,20,20,20,20,-33,-42,20,-38,-43,]),'[':([0,1,2,3,4,5,6,7,8,9,10,11,14,15,17,18,19,20,25,26,28,30,32,35,36,37,38,39,40,42,43,45,49,50,55,59,63,64,66,67,68,69,70,71,72,73,74,75,76,77,78,79,83,85,86,87,88,89,90,92,93,94,95,96,97,103,105,106,107,110,113,116,118,122,123,127,128,130,131,135,136,137,138,140,142,144,145,146,],[11,11,-1,-3,-4,-5,-6,-7,-8,29,-10,11,11,11,-58,11,-28,-29,11,-2,11,11,-50,65,-15,11,11,11,11,11,11,11,11,-27,-56,-12,-32,11,-16,-17,-18,-19,11,-21,11,-22,11,11,-60,11,-26,11,-39,-11,11,-9,11,110,-41,-31,-20,-23,-24,-25,65,11,11,11,-40,11,11,11,-57,133,11,-52,11,-37,11,11,11,11,11,-33,-42,11,-38,-43,]),'MAP':([0,1,2,3,4,5,6,7,8,10,11,14,15,17,18,19,20,25,26,28,30,32,35,36,37,38,39,40,42,43,45,49,50,55,59,63,64,66,67,68,69,70,71,72,73,74,75,76,77,78,79,83,85,86,87,88,90,92,93,94,95,96,103,105,106,107,110,113,116,118,123,127,128,130,131,135,136,137,138,140,142,144,145,146,],[21,21,-1,-3,-4,-5,-6,-7,-8,-10,21,21,21,-58,21,-28,-29,21,-2,21,21,-50,-30,-15,21,21,21,21,21,21,21,21,-27,-56,-12,-32,21,-16,-17,-18,-19,21,-21,21,-22,21,21,-60,21,-26,21,-39,-11,21,-9,21,-41,-31,-20,-23,-24,-25,21,21,21,-40,21,21,21,-57,21,-52,21,-37,21,21,21,21,21,-33,-42,21,-38,-43,]),'FOLD':([0,1,2,3,4,5,6,7,8,10,11,14,15,17,18,19,20,25,26,28,30,32,35,36,37,38,39,40,42,43,45,49,50,55,59,63,64,66,67,68,69,70,71,72,73,74,75,76,77,78,79,83,85,86,87,88,90,92,93,94,95,96,103,105,106,107,110,113,116,118,123,127,128,130,131,135,136,137,138,140,142,144,145,146,],[22,22,-1,-3,-4,-5,-6,-7,-8,-10,22,22,22,-58,22,-28,-29,22,-2,22,22,-50,-30,-15,22,22,22,22,22,22,22,22,-27,-56,-12,-32,22,-16,-17,-18,-19,22,-21,22,-22,22,22,-60,22,-26,22,-39,-11,22,-9,22,-41,-31,-20,-23,-24,-25,22,22,22,-40,22,22,22,-57,22,-52,22,-37,22,22,22,22,22,-33,-42,22,-38,-43,]),'ENTRADA':([0,1,2,3,4,5,6,7,8,10,11,14,15,17,18,19,20,25,26,28,30,32,35,36,37,38,39,40,42,43,45,49,50,55,59,63,64,66,67,68,69,70,71,72,73,74,75,76,77,78,79,83,85,86,87,88,90,92,93,94,95,96,103,105,106,107,110,113,116,118,123,127,128,130,131,135,136,137,138,140,142,144,145,146,],[23,23,-1,-3,-4,-5,-6,-7,-8,-10,23,23,23,-58,23,-28,-29,23,-2,23,23,-50,-30,-15,23,23,23,23,23,23,23,23,-27,-56,-12,-32,23,-16,-17,-18,-19,23,-21,23,-22,23,23,-60,23,-26,23,-39,-11,23,-9,23,-41,-31,-20,-23,-24,-25,23,23,23,-40,23,23,23,-57,23,-52,23,-37,23,23,23,23,23,-33,-42,23,-38,-43,]),'ALEATORIO':([0,1,2,3,4,5,6,7,8,10,11,14,15,17,18,19,20,25,26,28,30,32,35,36,37,38,39,40,42,43,45,49,50,55,59,63,64,66,67,68,69,70,71,72,73,74,75,76,77,78,79,83,85,86,87,88,90,92,93,94,95,96,103,105,106,107,110,113,116,118,123,127,128,130,131,135,136,137,138,140,142,144,145,146,],[24,24,-1,-3,-4,-5,-6,-7,-8,-10,24,24,24,-58,24,-28,-29,24,-2,24,24,-50,-30,-15,24,24,24,24,24,24,24,24,-27,-56,-12,-32,24,-16,-17,-18,-19,24,-21,24,-22,24,24,-60,24,-26,24,-39,-11,24,-9,24,-41,-31,-20,-23,-24,-25,24,24,24,-40,24,24,24,-57,24,-52,24,-37,24,24,24,24,24,-33,-42,24,-38,-43,]),'NEG':([0,1,2,3,4,5,6,7,8,10,11,14,15,17,18,19,20,25,26,28,30,32,35,36,37,38,39,40,42,43,45,49,50,55,59,63,64,66,67,68,69,70,71,72,73,74,75,76,77,78,79,83,85,86,87,88,90,92,93,94,95,96,103,105,106,107,110,113,116,118,123,127,128,130,131,135,136,137,138,140,142,144,145,146,],[25,25,-1,-3,-4,-5,-6,-7,-8,-10,25,25,25,-58,25,-28,-29,25,-2,25,25,-50,-30,-15,25,25,25,25,25,25,25,25,-27,-56,-12,-32,25,-16,-17,-18,-19,25,-21,25,-22,25,25,-60,25,-26,25,-39,-11,25,-9,25,-41,-31,-20,-23,-24,-25,25,25,25,-40,25,25,25,-57,25,-52,25,-37,25,25,25,25,25,-33,-42,25,-38,-43,]),'$end':([1,2,3,4,5,6,7,8,10,17,19,20,26,32,35,36,50,55,59,63,66,67,68,69,71,73,76,78,83,85,87,90,92,93,94,95,96,107,118,127,130,140,142,145,146,],[0,-1,-3,-4,-5,-6,-7,-8,-10,-58,-28,-29,-2,-50,-30,-15,-27,-56,-12,-32,-16,-17,-18,-19,-21,-22,-60,-26,-39,-11,-9,-41,-31,-20,-23,-24,-25,-40,-57,-52,-37,-33,-42,-38,-43,]),'SENAO':([2,3,4,5,6,7,8,10,17,19,20,26,32,35,36,50,55,59,63,66,67,68,69,71,73,76,78,83,85,87,90,92,93,94,95,96,103,107,118,127,130,140,142,145,146,],[-1,-3,-4,-5,-6,-7,-8,-10,-58,-28,-29,-2,-50,-30,-15,-27,-56,-12,-32,-16,-17,-18,-19,-21,-22,-60,-26,-39,-11,-9,-41,-31,-20,-23,-24,-25,115,-40,-57,-52,-37,-33,-42,-38,-43,]),'SENAOSE':([2,3,4,5,6,7,8,10,17,19,20,26,32,35,36,50,55,59,63,66,67,68,69,71,73,76,78,83,85,87,90,92,93,94,95,96,103,107,118,127,130,140,142,145,146,],[-1,-3,-4,-5,-6,-7,-8,-10,-58,-28,-29,-2,-50,-30,-15,-27,-56,-12,-32,-16,-17,-18,-19,-21,-22,-60,-26,-39,-11,-9,-41,-31,-20,-23,-24,-25,116,-40,-57,-52,-37,-33,-42,-38,-43,]),'FIM':([2,3,4,5,6,7,8,10,17,19,20,26,32,35,36,50,55,59,63,66,67,68,69,71,73,76,78,83,85,87,90,92,93,94,95,96,103,107,114,117,118,127,130,134,135,137,140,142,144,145,146,],[-1,-3,-4,-5,-6,-7,-8,-10,-58,-28,-29,-2,-50,-30,-15,-27,-56,-12,-32,-16,-17,-18,-19,-21,-22,-60,-26,-39,-11,-9,-41,-31,-20,-23,-24,-25,-59,-40,127,-55,-57,-52,-37,142,-61,-53,-33,-42,-54,-38,-43,]),',':([3,10,11,19,20,31,32,33,34,35,50,55,58,59,61,62,63,66,67,68,69,71,73,76,78,81,82,83,85,87,90,91,92,93,94,95,96,97,99,100,102,107,109,110,112,119,120,121,125,126,130,139,140,141,145,],[27,-10,-59,-28,-29,64,-50,-35,-36,-30,-27,-56,88,-12,88,-14,-32,-16,-17,-18,-19,-21,-22,-60,-26,105,106,-39,-11,-9,-41,-34,-31,-20,-23,-24,-25,-30,-48,113,-49,-40,-13,-59,124,88,131,64,-46,-47,-37,-13,-33,-51,-38,]),'=':([9,12,19,20,32,33,35,41,42,43,44,47,48,50,55,57,59,60,62,63,66,67,68,69,71,73,76,78,80,83,90,91,92,93,94,95,96,97,99,107,108,109,125,129,130,139,143,145,],[28,41,-28,-29,-50,41,-30,70,72,74,75,41,41,-27,-56,86,41,89,41,-32,-16,-17,-18,-19,41,41,41,-26,41,-39,-41,41,-31,41,41,41,41,-30,41,-40,41,41,41,41,-37,41,41,-38,]),';':([9,12,19,20,32,35,50,55,56,58,59,60,63,66,67,68,69,71,73,76,78,83,90,92,93,94,95,96,104,107,108,109,130,132,143,145,],[-30,36,-28,-29,-50,-30,-27,-56,85,87,-14,-31,-32,-16,-17,-18,-19,-21,-22,-60,-26,-39,-41,-31,-20,-23,-24,-25,118,-40,-12,-13,-37,140,146,-38,]),'+':([9,12,19,20,32,33,35,47,48,50,55,59,60,62,63,66,67,68,69,71,73,76,78,80,83,90,91,92,93,94,95,96,97,99,107,108,109,125,129,130,139,143,145,],[-30,37,-28,-29,-50,37,-30,37,37,-27,-56,37,-31,37,-32,-16,-17,-18,-19,37,37,37,-26,37,-39,-41,37,-31,37,37,37,37,-30,37,-40,37,37,37,37,-37,37,37,-38,]),'*':([9,12,19,20,32,33,35,47,48,50,55,59,60,62,63,66,67,68,69,71,73,76,78,80,83,90,91,92,93,94,95,96,97,99,107,108,109,125,129,130,139,143,145,],[-30,39,-28,-29,-50,39,-30,39,39,-27,-56,39,-31,39,-32,39,39,-18,-19,39,39,39,-26,39,-39,-41,39,-31,39,39,39,39,-30,39,-40,39,39,39,39,-37,39,39,-38,]),'/':([9,12,19,20,32,33,35,47,48,50,55,59,60,62,63,66,67,68,69,71,73,76,78,80,83,90,91,92,93,94,95,96,97,99,107,108,109,125,129,130,139,143,145,],[-30,40,-28,-29,-50,40,-30,40,40,-27,-56,40,-31,40,-32,40,40,-18,-19,40,40,40,-26,40,-39,-41,40,-31,40,40,40,40,-30,40,-40,40,40,40,40,-37,40,40,-38,]),'<':([9,12,19,20,32,33,35,47,48,50,55,59,60,62,63,66,67,68,69,71,73,76,78,80,83,90,91,92,93,94,95,96,97,99,107,108,109,125,129,130,139,143,145,],[-30,42,-28,-29,-50,42,-30,42,42,-27,-56,42,-31,42,-32,-16,-17,-18,-19,42,42,42,-26,42,-39,-41,42,-31,42,42,42,42,-30,42,-40,42,42,42,42,-37,42,42,-38,]),'>':([9,12,19,20,32,33,35,47,48,50,55,59,60,62,63,66,67,68,69,71,73,76,78,80,83,90,91,92,93,94,95,96,97,99,107,108,109,125,129,130,139,143,145,],[-30,43,-28,-29,-50,43,-30,43,43,-27,-56,43,-31,43,-32,-16,-17,-18,-19,43,43,43,-26,43,-39,-41,43,-31,43,43,43,43,-30,43,-40,43,43,43,43,-37,43,43,-38,]),'!':([9,12,19,20,32,33,35,47,48,50,55,59,60,62,63,66,67,68,69,71,73,76,78,80,83,90,91,92,93,94,95,96,97,99,107,108,109,125,129,130,139,143,145,],[-30,44,-28,-29,-50,44,-30,44,44,-27,-56,44,-31,44,-32,-16,-17,-18,-19,44,44,44,-26,44,-39,-41,44,-31,44,44,44,44,-30,44,-40,44,44,44,44,-37,44,44,-38,]),'CONCAT':([9,12,19,20,32,33,35,47,48,50,55,59,60,62,63,66,67,68,69,71,73,76,78,80,83,90,91,92,93,94,95,96,97,99,107,108,109,125,129,130,139,143,145,],[-30,45,-28,-29,-50,45,-30,45,45,-27,-56,45,-31,45,-32,-16,-17,-18,-19,45,45,45,-26,45,-39,-41,45,-31,45,45,45,45,-30,45,-40,45,45,45,45,-37,45,45,-38,]),']':([11,19,20,29,31,32,33,34,35,50,55,63,65,66,67,68,69,71,73,76,78,83,90,91,92,93,94,95,96,107,110,121,130,133,145,],[32,-28,-29,60,63,-50,-35,-36,-30,-27,-56,-32,92,-16,-17,-18,-19,-21,-22,-60,-26,-39,-41,-34,-31,-20,-23,-24,-25,-40,-59,132,-37,141,-38,]),')':([19,20,32,35,47,50,53,55,61,62,63,66,67,68,69,71,73,76,77,78,80,83,84,90,92,93,94,95,96,97,98,99,100,101,102,107,109,119,125,126,130,139,141,145,],[-28,-29,-50,-30,78,-27,83,-56,90,-14,-32,-16,-17,-18,-19,-21,-22,-60,-59,-26,104,-39,107,-41,-31,-20,-23,-24,-25,-30,112,-48,-44,-45,-49,-40,-13,130,-46,-47,-37,145,-51,-38,]),':':([19,20,32,35,48,50,55,63,66,67,68,69,71,73,76,78,83,90,92,93,94,95,96,97,107,112,115,124,129,130,145,],[-28,-29,-50,-30,79,-27,-56,-32,-16,-17,-18,-19,-21,-22,-60,-26,-39,-41,-31,-20,-23,-24,-25,111,-40,123,128,136,138,-37,-38,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'lista_declaracoes':([0,79,123,128,138,],[1,103,135,137,144,]),'declaracao':([0,1,79,103,123,128,135,137,138,144,],[2,26,2,26,2,2,26,26,2,26,]),'declaracao_atribuicao':([0,1,79,103,123,128,135,137,138,144,],[3,3,3,3,3,3,3,3,3,3,]),'declaracao_expressao':([0,1,79,103,123,128,135,137,138,144,],[4,4,4,4,4,4,4,4,4,4,]),'declaracao_funcao':([0,1,79,103,123,128,135,137,138,144,],[5,5,5,5,5,5,5,5,5,5,]),'declaracao_se':([0,1,79,103,123,128,135,137,138,144,],[6,6,6,6,6,6,6,6,6,6,]),'declaracao_escrever':([0,1,79,103,123,128,135,137,138,144,],[7,7,7,7,7,7,7,7,7,7,]),'declaracao_comentario':([0,1,79,103,123,128,135,137,138,144,],[8,8,8,8,8,8,8,8,8,8,]),'atribuicao':([0,1,27,79,103,123,128,135,137,138,144,],[10,10,56,10,10,10,10,10,10,10,10,]),'expressao':([0,1,11,14,15,18,25,28,30,37,38,39,40,42,43,45,49,64,70,72,74,75,77,79,86,88,103,105,106,110,113,116,123,128,131,135,136,137,138,144,],[12,12,33,47,48,50,55,59,62,66,67,68,69,71,73,76,80,91,93,94,95,96,99,12,108,109,12,62,62,33,125,129,12,12,139,12,143,12,12,12,]),'lista_elementos':([11,110,],[31,121,]),'vazio':([11,77,103,110,],[34,101,117,34,]),'lista_expressoes':([28,30,105,106,],[58,61,119,120,]),'lista_parametros_opcional':([77,],[98,]),'lista_parametros':([77,],[100,]),'var_id_array':([77,113,],[102,126,]),'senao':([103,],[114,]),'bloco_funcao':([123,],[134,]),}

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
  ('declaracao_atribuicao -> atribuicao','declaracao_atribuicao',1,'p_declaracao_atribuicao_multipla','arith_grammar.py',62),
  ('declaracao_atribuicao -> declaracao_atribuicao , atribuicao ;','declaracao_atribuicao',4,'p_declaracao_atribuicao_multipla','arith_grammar.py',63),
  ('atribuicao -> VAR_ID = expressao','atribuicao',3,'p_atribuicao','arith_grammar.py',77),
  ('lista_expressoes -> lista_expressoes , expressao','lista_expressoes',3,'p_lista_expressoes','arith_grammar.py',81),
  ('lista_expressoes -> expressao','lista_expressoes',1,'p_lista_expressoes','arith_grammar.py',82),
  ('declaracao_expressao -> expressao ;','declaracao_expressao',2,'p_declaracao_expressao','arith_grammar.py',93),
  ('expressao -> expressao + expressao','expressao',3,'p_expressao','arith_grammar.py',98),
  ('expressao -> expressao - expressao','expressao',3,'p_expressao','arith_grammar.py',99),
  ('expressao -> expressao * expressao','expressao',3,'p_expressao','arith_grammar.py',100),
  ('expressao -> expressao / expressao','expressao',3,'p_expressao','arith_grammar.py',101),
  ('expressao -> expressao = = expressao','expressao',4,'p_expressao','arith_grammar.py',102),
  ('expressao -> expressao < expressao','expressao',3,'p_expressao','arith_grammar.py',103),
  ('expressao -> expressao > expressao','expressao',3,'p_expressao','arith_grammar.py',104),
  ('expressao -> expressao < = expressao','expressao',4,'p_expressao','arith_grammar.py',105),
  ('expressao -> expressao > = expressao','expressao',4,'p_expressao','arith_grammar.py',106),
  ('expressao -> expressao ! = expressao','expressao',4,'p_expressao','arith_grammar.py',107),
  ('expressao -> ( expressao )','expressao',3,'p_expressao_grupo','arith_grammar.py',116),
  ('expressao -> - expressao','expressao',2,'p_expressao_uminus','arith_grammar.py',121),
  ('expressao -> NUM','expressao',1,'p_expressao_num','arith_grammar.py',126),
  ('expressao -> STRING','expressao',1,'p_expressao_string','arith_grammar.py',135),
  ('expressao -> VAR_ID','expressao',1,'p_expressao_var_id','arith_grammar.py',156),
  ('expressao -> VAR_ID [ ]','expressao',3,'p_expressao_var_array','arith_grammar.py',161),
  ('expressao -> [ lista_elementos ]','expressao',3,'p_expressao_array','arith_grammar.py',166),
  ('declaracao_atribuicao -> VAR_ID [ ] = [ lista_elementos ] ;','declaracao_atribuicao',8,'p_expressao_array_init','arith_grammar.py',171),
  ('lista_elementos -> lista_elementos , expressao','lista_elementos',3,'p_lista_elementos','arith_grammar.py',176),
  ('lista_elementos -> expressao','lista_elementos',1,'p_lista_elementos','arith_grammar.py',177),
  ('lista_elementos -> vazio','lista_elementos',1,'p_lista_elementos','arith_grammar.py',178),
  ('expressao -> MAP ( VAR_ID , lista_expressoes )','expressao',6,'p_expressao_map','arith_grammar.py',190),
  ('expressao -> FOLD ( VAR_ID , lista_expressoes , expressao )','expressao',8,'p_expressao_fold','arith_grammar.py',195),
  ('expressao -> ENTRADA ( )','expressao',3,'p_expressao_entrada','arith_grammar.py',200),
  ('expressao -> ALEATORIO ( NUM )','expressao',4,'p_expressao_aleatorio','arith_grammar.py',205),
  ('expressao -> VAR_ID ( lista_expressoes )','expressao',4,'p_expressao_chamada_funcao','arith_grammar.py',210),
  ('declaracao_funcao -> FUNCAO VAR_ID ( lista_parametros_opcional ) : bloco_funcao FIM','declaracao_funcao',8,'p_declaracao_funcao','arith_grammar.py',218),
  ('declaracao_funcao -> FUNCAO VAR_ID ( lista_parametros_opcional ) , : expressao ;','declaracao_funcao',9,'p_declaracao_funcao','arith_grammar.py',219),
  ('lista_parametros_opcional -> lista_parametros','lista_parametros_opcional',1,'p_lista_parametros_opcional','arith_grammar.py',228),
  ('lista_parametros_opcional -> vazio','lista_parametros_opcional',1,'p_lista_parametros_opcional','arith_grammar.py',229),
  ('lista_parametros -> lista_parametros , expressao','lista_parametros',3,'p_lista_parametros','arith_grammar.py',234),
  ('lista_parametros -> lista_parametros , var_id_array','lista_parametros',3,'p_lista_parametros','arith_grammar.py',235),
  ('lista_parametros -> expressao','lista_parametros',1,'p_lista_parametros','arith_grammar.py',236),
  ('lista_parametros -> var_id_array','lista_parametros',1,'p_lista_parametros','arith_grammar.py',237),
  ('expressao -> [ ]','expressao',2,'p_empty_list','arith_grammar.py',246),
  ('var_id_array -> VAR_ID : VAR_ID [ ]','var_id_array',5,'p_var_array','arith_grammar.py',251),
  ('declaracao_se -> SE expressao : lista_declaracoes senao FIM','declaracao_se',6,'p_declaracao_se','arith_grammar.py',257),
  ('senao -> SENAO : lista_declaracoes','senao',3,'p_senao_opcional','arith_grammar.py',262),
  ('senao -> SENAOSE expressao : lista_declaracoes','senao',4,'p_senao_opcional','arith_grammar.py',263),
  ('senao -> vazio','senao',1,'p_senao_opcional','arith_grammar.py',264),
  ('expressao -> NEG expressao','expressao',2,'p_expressao_negacao','arith_grammar.py',275),
  ('declaracao_escrever -> ESCREVER ( expressao ) ;','declaracao_escrever',5,'p_declaracao_escrever','arith_grammar.py',280),
  ('declaracao_comentario -> COMENTARIO','declaracao_comentario',1,'p_declaracao_comentario','arith_grammar.py',285),
  ('vazio -> <empty>','vazio',0,'p_vazio','arith_grammar.py',290),
  ('expressao -> expressao CONCAT expressao','expressao',3,'p_expressao_concat','arith_grammar.py',295),
  ('bloco_funcao -> lista_declaracoes','bloco_funcao',1,'p_bloco_funcao','arith_grammar.py',300),
]
