
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'rightIDMODULEIMPORTSrightIGUALrightUPDATErightNUMEROleftNOIGUALleftMENORQMAYORQleftSUMARESTAleftMULTIDIVrightPUNTOleftPIZQPDERleftLLIZQLLDERARGS AS BEGIN BOOLEAN CONSOLE DATETIME DIM DIV END FALSE ID IGUAL IMPORTS LLDER LLIZQ MAIN MAYORQ MENORQ MOD MODULE MULTI NOIGUAL NOW NUMERO PDER PIZQ PROGRAM PUNTO READKEY READLINE RESTA STRING SUB SUMA TRUE UPDATE VBCRLF WRITELINEmodule : programprogram : constDecl varDecl procDecl statementargs : ARGSimports : IMPORTS IDconstDecl : DIM constAssignmentListconstDecl : DIM ID IGUAL IDconstDecl : DIM ID AS ID IGUAL IDconstDecl : emptyconstAssignmentList : ID IGUAL NUMEROconstAssignmentList : constAssignmentList ID IGUAL NUMEROvarDecl : DIM identListvarDecl : emptyidentList : IDidentList : identList IDprocDecl : emptystatement : ID UPDATE expressionstatement : IDstatement : BEGIN statementList ENDstatement : conditionstatement : IMPORTS IDstatement : emptystatementList : statementstatementList : statementList statementcondition : expressioncondition : expression relation expressionrelation : IGUALrelation : NOIGUALrelation : MENORQrelation : MAYORQrelation : TRUErelation : FALSEexpression : termexpression : multiplyingOperator termexpression : addingOperator termexpression : expression addingOperator term expressionexpression : DATETIME PUNTO NOWexpression : LLIZQ ID LLDERexpression : VBCRLFexpression : MODULE PROGRAMexpression : END MODULEexpression : CONSOLE PUNTO READKEY PIZQ boolean PDERexpression : DIM ID IGUAL CONSOLE PUNTO READLINE PIZQ PDERexpression : CONSOLE PUNTO WRITELINE PIZQ ID PDERexpression : DIM ID AS BOOLEAN IGUAL termexpression : ID IGUAL expressionaddingOperator : SUMAaddingOperator : RESTAaddingOperator : MODterm : factorterm : term multiplyingOperator factorterm : PIZQ NUMERO MAYORQ NUMERO PDERterm : BOOLEAN IGUAL termterm : term addingOperator factormultiplyingOperator : MULTImultiplyingOperator : DIVfactor : IDfactor : NUMEROfactor : PIZQ expression PDERboolean : BOOLEANempty :'
    
_lr_action_items = {'DIM':([0,3,5,6,8,9,11,12,13,14,19,20,21,23,25,26,31,34,37,38,44,46,47,49,50,51,53,54,55,56,57,58,59,60,61,62,65,66,67,70,74,77,79,80,81,82,83,84,85,86,87,88,89,93,96,97,98,106,107,108,112,115,116,118,120,],[4,7,-8,-60,-12,-5,35,-15,-11,-13,-17,-24,35,-19,-21,-32,-38,35,-49,-57,-14,-6,-9,35,35,35,-26,-27,-28,-29,-30,-31,35,-22,-40,-20,-33,-56,-34,-39,-56,-10,-16,-45,-25,35,-18,-23,-50,35,-53,-36,-37,-58,-52,-7,-35,-49,35,-49,-51,-41,-43,-44,-42,]),'ID':([0,3,4,5,6,7,8,9,11,12,13,14,16,17,19,20,21,23,24,25,26,27,28,30,31,34,35,37,38,39,40,41,42,43,44,46,47,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,70,74,76,77,78,79,80,81,82,83,84,85,86,87,88,89,93,96,97,98,99,100,102,106,107,108,112,114,115,116,118,120,],[-60,-60,10,-8,-60,14,-12,15,19,-15,44,-13,46,48,-17,-24,19,-19,62,-21,-32,66,66,69,-38,74,75,-49,-57,-54,-55,-46,-47,-48,-14,-6,-9,74,74,74,66,-26,-27,-28,-29,-30,-31,19,-22,-40,-20,66,66,-33,-56,-34,-39,-56,66,-10,97,-16,-45,-25,74,-18,-23,-50,74,-53,-36,-37,-58,-52,-7,-35,66,66,111,-49,74,-49,-51,66,-41,-43,-44,-42,]),'BEGIN':([0,3,5,6,8,9,11,12,13,14,19,20,21,23,25,26,31,37,38,44,46,47,59,60,61,62,65,66,67,70,74,77,79,80,81,83,84,85,87,88,89,93,96,97,98,106,108,112,115,116,118,120,],[-60,-60,-8,-60,-12,-5,21,-15,-11,-13,-17,-24,21,-19,-21,-32,-38,-49,-57,-14,-6,-9,21,-22,-40,-20,-33,-56,-34,-39,-56,-10,-16,-45,-25,-18,-23,-50,-53,-36,-37,-58,-52,-7,-35,-49,-49,-51,-41,-43,-44,-42,]),'IMPORTS':([0,3,5,6,8,9,11,12,13,14,19,20,21,23,25,26,31,37,38,44,46,47,59,60,61,62,65,66,67,70,74,77,79,80,81,83,84,85,87,88,89,93,96,97,98,106,108,112,115,116,118,120,],[-60,-60,-8,-60,-12,-5,24,-15,-11,-13,-17,-24,24,-19,-21,-32,-38,-49,-57,-14,-6,-9,24,-22,-40,-20,-33,-56,-34,-39,-56,-10,-16,-45,-25,-18,-23,-50,-53,-36,-37,-58,-52,-7,-35,-49,-49,-51,-41,-43,-44,-42,]),'DATETIME':([0,3,5,6,8,9,11,12,13,14,19,20,21,23,25,26,31,34,37,38,44,46,47,49,50,51,53,54,55,56,57,58,59,60,61,62,65,66,67,70,74,77,79,80,81,82,83,84,85,86,87,88,89,93,96,97,98,106,107,108,112,115,116,118,120,],[-60,-60,-8,-60,-12,-5,29,-15,-11,-13,-17,-24,29,-19,-21,-32,-38,29,-49,-57,-14,-6,-9,29,29,29,-26,-27,-28,-29,-30,-31,29,-22,-40,-20,-33,-56,-34,-39,-56,-10,-16,-45,-25,29,-18,-23,-50,29,-53,-36,-37,-58,-52,-7,-35,-49,29,-49,-51,-41,-43,-44,-42,]),'LLIZQ':([0,3,5,6,8,9,11,12,13,14,19,20,21,23,25,26,31,34,37,38,44,46,47,49,50,51,53,54,55,56,57,58,59,60,61,62,65,66,67,70,74,77,79,80,81,82,83,84,85,86,87,88,89,93,96,97,98,106,107,108,112,115,116,118,120,],[-60,-60,-8,-60,-12,-5,30,-15,-11,-13,-17,-24,30,-19,-21,-32,-38,30,-49,-57,-14,-6,-9,30,30,30,-26,-27,-28,-29,-30,-31,30,-22,-40,-20,-33,-56,-34,-39,-56,-10,-16,-45,-25,30,-18,-23,-50,30,-53,-36,-37,-58,-52,-7,-35,-49,30,-49,-51,-41,-43,-44,-42,]),'VBCRLF':([0,3,5,6,8,9,11,12,13,14,19,20,21,23,25,26,31,34,37,38,44,46,47,49,50,51,53,54,55,56,57,58,59,60,61,62,65,66,67,70,74,77,79,80,81,82,83,84,85,86,87,88,89,93,96,97,98,106,107,108,112,115,116,118,120,],[-60,-60,-8,-60,-12,-5,31,-15,-11,-13,-17,-24,31,-19,-21,-32,-38,31,-49,-57,-14,-6,-9,31,31,31,-26,-27,-28,-29,-30,-31,31,-22,-40,-20,-33,-56,-34,-39,-56,-10,-16,-45,-25,31,-18,-23,-50,31,-53,-36,-37,-58,-52,-7,-35,-49,31,-49,-51,-41,-43,-44,-42,]),'MODULE':([0,3,5,6,8,9,11,12,13,14,19,20,21,22,23,25,26,31,34,37,38,44,46,47,49,50,51,53,54,55,56,57,58,59,60,61,62,65,66,67,70,74,77,79,80,81,82,83,84,85,86,87,88,89,93,96,97,98,106,107,108,112,115,116,118,120,],[-60,-60,-8,-60,-12,-5,32,-15,-11,-13,-17,-24,32,61,-19,-21,-32,-38,32,-49,-57,-14,-6,-9,32,32,32,-26,-27,-28,-29,-30,-31,32,-22,-40,-20,-33,-56,-34,-39,-56,-10,-16,-45,-25,32,61,-23,-50,32,-53,-36,-37,-58,-52,-7,-35,-49,32,-49,-51,-41,-43,-44,-42,]),'END':([0,3,5,6,8,9,11,12,13,14,19,20,21,23,25,26,31,34,37,38,44,46,47,49,50,51,53,54,55,56,57,58,59,60,61,62,65,66,67,70,74,77,79,80,81,82,83,84,85,86,87,88,89,93,96,97,98,106,107,108,112,115,116,118,120,],[-60,-60,-8,-60,-12,-5,22,-15,-11,-13,-17,-24,22,-19,-21,-32,-38,22,-49,-57,-14,-6,-9,22,22,22,-26,-27,-28,-29,-30,-31,83,-22,-40,-20,-33,-56,-34,-39,-56,-10,-16,-45,-25,22,-18,-23,-50,22,-53,-36,-37,-58,-52,-7,-35,-49,22,-49,-51,-41,-43,-44,-42,]),'CONSOLE':([0,3,5,6,8,9,11,12,13,14,19,20,21,23,25,26,31,34,37,38,44,46,47,49,50,51,53,54,55,56,57,58,59,60,61,62,65,66,67,70,74,77,79,80,81,82,83,84,85,86,87,88,89,93,94,96,97,98,106,107,108,112,115,116,118,120,],[-60,-60,-8,-60,-12,-5,33,-15,-11,-13,-17,-24,33,-19,-21,-32,-38,33,-49,-57,-14,-6,-9,33,33,33,-26,-27,-28,-29,-30,-31,33,-22,-40,-20,-33,-56,-34,-39,-56,-10,-16,-45,-25,33,-18,-23,-50,33,-53,-36,-37,-58,104,-52,-7,-35,-49,33,-49,-51,-41,-43,-44,-42,]),'PIZQ':([0,3,5,6,8,9,11,12,13,14,19,20,21,23,25,26,27,28,31,34,37,38,39,40,41,42,43,44,46,47,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,70,74,76,77,79,80,81,82,83,84,85,86,87,88,89,90,91,93,96,97,98,99,100,106,107,108,112,114,115,116,117,118,120,],[-60,-60,-8,-60,-12,-5,34,-15,-11,-13,-17,-24,34,-19,-21,-32,34,34,-38,34,-49,-57,-54,-55,-46,-47,-48,-14,-6,-9,34,34,34,34,-26,-27,-28,-29,-30,-31,34,-22,-40,-20,86,86,-33,-56,-34,-39,-56,34,-10,-16,-45,-25,34,-18,-23,-50,34,-53,-36,-37,101,102,-58,-52,-7,-35,107,107,-49,34,-49,-51,34,-41,-43,119,-44,-42,]),'BOOLEAN':([0,3,5,6,8,9,11,12,13,14,19,20,21,23,25,26,27,28,31,34,37,38,39,40,41,42,43,44,46,47,49,50,51,52,53,54,55,56,57,58,59,60,61,62,65,66,67,70,74,76,77,79,80,81,82,83,84,85,86,87,88,89,93,95,96,97,98,99,100,101,106,107,108,112,114,115,116,118,120,],[-60,-60,-8,-60,-12,-5,36,-15,-11,-13,-17,-24,36,-19,-21,-32,36,36,-38,36,-49,-57,-54,-55,-46,-47,-48,-14,-6,-9,36,36,36,36,-26,-27,-28,-29,-30,-31,36,-22,-40,-20,-33,-56,-34,-39,-56,36,-10,-16,-45,-25,36,-18,-23,-50,36,-53,-36,-37,-58,105,-52,-7,-35,36,36,110,-49,36,-49,-51,36,-41,-43,-44,-42,]),'MULTI':([0,3,5,6,8,9,11,12,13,14,19,20,21,23,25,26,31,34,37,38,44,46,47,49,50,51,53,54,55,56,57,58,59,60,61,62,65,66,67,70,72,74,77,79,80,81,82,83,84,85,86,87,88,89,93,96,97,98,106,107,108,112,115,116,118,120,],[-60,-60,-8,-60,-12,-5,39,-15,-11,-13,-17,-24,39,-19,-21,39,-38,39,-49,-57,-14,-6,-9,39,39,39,-26,-27,-28,-29,-30,-31,39,-22,-40,-20,39,-56,39,-39,-57,-56,-10,-16,-45,-25,39,-18,-23,-50,39,-53,-36,-37,-58,39,-7,-35,-49,39,-49,-51,-41,-43,39,-42,]),'DIV':([0,3,5,6,8,9,11,12,13,14,19,20,21,23,25,26,31,34,37,38,44,46,47,49,50,51,53,54,55,56,57,58,59,60,61,62,65,66,67,70,72,74,77,79,80,81,82,83,84,85,86,87,88,89,93,96,97,98,106,107,108,112,115,116,118,120,],[-60,-60,-8,-60,-12,-5,40,-15,-11,-13,-17,-24,40,-19,-21,40,-38,40,-49,-57,-14,-6,-9,40,40,40,-26,-27,-28,-29,-30,-31,40,-22,-40,-20,40,-56,40,-39,-57,-56,-10,-16,-45,-25,40,-18,-23,-50,40,-53,-36,-37,-58,40,-7,-35,-49,40,-49,-51,-41,-43,40,-42,]),'SUMA':([0,3,5,6,8,9,11,12,13,14,19,20,21,23,25,26,31,34,37,38,44,46,47,49,50,51,53,54,55,56,57,58,59,60,61,62,65,66,67,70,72,73,74,77,79,80,81,82,83,84,85,86,87,88,89,93,96,97,98,106,107,108,112,115,116,118,120,],[-60,-60,-8,-60,-12,-5,41,-15,-11,-13,-17,41,41,-19,-21,41,-38,41,-49,-57,-14,-6,-9,41,41,41,-26,-27,-28,-29,-30,-31,41,-22,-40,-20,41,-56,41,-39,-57,41,-56,-10,41,41,41,41,-18,-23,-50,41,-53,-36,-37,-58,41,-7,41,-49,41,-49,-51,-41,-43,41,-42,]),'RESTA':([0,3,5,6,8,9,11,12,13,14,19,20,21,23,25,26,31,34,37,38,44,46,47,49,50,51,53,54,55,56,57,58,59,60,61,62,65,66,67,70,72,73,74,77,79,80,81,82,83,84,85,86,87,88,89,93,96,97,98,106,107,108,112,115,116,118,120,],[-60,-60,-8,-60,-12,-5,42,-15,-11,-13,-17,42,42,-19,-21,42,-38,42,-49,-57,-14,-6,-9,42,42,42,-26,-27,-28,-29,-30,-31,42,-22,-40,-20,42,-56,42,-39,-57,42,-56,-10,42,42,42,42,-18,-23,-50,42,-53,-36,-37,-58,42,-7,42,-49,42,-49,-51,-41,-43,42,-42,]),'MOD':([0,3,5,6,8,9,11,12,13,14,19,20,21,23,25,26,31,34,37,38,44,46,47,49,50,51,53,54,55,56,57,58,59,60,61,62,65,66,67,70,72,73,74,77,79,80,81,82,83,84,85,86,87,88,89,93,96,97,98,106,107,108,112,115,116,118,120,],[-60,-60,-8,-60,-12,-5,43,-15,-11,-13,-17,43,43,-19,-21,43,-38,43,-49,-57,-14,-6,-9,43,43,43,-26,-27,-28,-29,-30,-31,43,-22,-40,-20,43,-56,43,-39,-57,43,-56,-10,-16,-45,43,43,-18,-23,-50,43,-53,-36,-37,-58,-52,-7,43,-49,43,-49,-51,-41,-43,-44,-42,]),'NUMERO':([0,3,5,6,8,9,11,12,13,14,16,19,20,21,23,25,26,27,28,31,34,37,38,39,40,41,42,43,44,45,46,47,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,70,74,76,77,79,80,81,82,83,84,85,86,87,88,89,92,93,96,97,98,99,100,106,107,108,112,114,115,116,118,120,],[-60,-60,-8,-60,-12,-5,38,-15,-11,-13,47,-17,-24,38,-19,-21,-32,38,38,-38,72,-49,-57,-54,-55,-46,-47,-48,-14,77,-6,-9,38,38,38,38,-26,-27,-28,-29,-30,-31,38,-22,-40,-20,38,38,-33,-56,-34,-39,-56,38,-10,-16,-45,-25,38,-18,-23,-50,38,-53,-36,-37,103,-58,-52,-7,-35,38,38,-49,72,-49,-51,38,-41,-43,-44,-42,]),'$end':([0,1,2,3,5,6,8,9,11,12,13,14,18,19,20,23,25,26,31,37,38,44,46,47,61,62,65,66,67,70,74,77,79,80,81,83,85,87,88,89,93,96,97,98,106,108,112,115,116,118,120,],[-60,0,-1,-60,-8,-60,-12,-5,-60,-15,-11,-13,-2,-17,-24,-19,-21,-32,-38,-49,-57,-14,-6,-9,-40,-20,-33,-56,-34,-39,-56,-10,-16,-45,-25,-18,-50,-53,-36,-37,-58,-52,-7,-35,-49,-49,-51,-41,-43,-44,-42,]),'IGUAL':([10,15,19,20,26,31,36,37,38,48,61,65,66,67,70,74,75,80,85,87,88,89,93,96,98,105,106,108,112,115,116,118,120,],[16,45,50,53,-32,-38,76,-49,-57,78,-40,-33,-56,-34,-39,50,94,-45,-50,-53,-36,-37,-58,-52,-35,114,-49,-49,-51,-41,-43,-44,-42,]),'AS':([10,75,],[17,95,]),'UPDATE':([19,],[49,]),'NOIGUAL':([19,20,26,31,37,38,61,65,66,67,70,74,80,85,87,88,89,93,96,98,106,108,112,115,116,118,120,],[-56,54,-32,-38,-49,-57,-40,-33,-56,-34,-39,-56,-45,-50,-53,-36,-37,-58,-52,-35,-49,-49,-51,-41,-43,-44,-42,]),'MENORQ':([19,20,26,31,37,38,61,65,66,67,70,74,80,85,87,88,89,93,96,98,106,108,112,115,116,118,120,],[-56,55,-32,-38,-49,-57,-40,-33,-56,-34,-39,-56,-45,-50,-53,-36,-37,-58,-52,-35,-49,-49,-51,-41,-43,-44,-42,]),'MAYORQ':([19,20,26,31,37,38,61,65,66,67,70,72,74,80,85,87,88,89,93,96,98,106,108,112,115,116,118,120,],[-56,56,-32,-38,-49,-57,-40,-33,-56,-34,-39,92,-56,-45,-50,-53,-36,-37,-58,-52,-35,-49,-49,-51,-41,-43,-44,-42,]),'TRUE':([19,20,26,31,37,38,61,65,66,67,70,74,80,85,87,88,89,93,96,98,106,108,112,115,116,118,120,],[-56,57,-32,-38,-49,-57,-40,-33,-56,-34,-39,-56,-45,-50,-53,-36,-37,-58,-52,-35,-49,-49,-51,-41,-43,-44,-42,]),'FALSE':([19,20,26,31,37,38,61,65,66,67,70,74,80,85,87,88,89,93,96,98,106,108,112,115,116,118,120,],[-56,58,-32,-38,-49,-57,-40,-33,-56,-34,-39,-56,-45,-50,-53,-36,-37,-58,-52,-35,-49,-49,-51,-41,-43,-44,-42,]),'PDER':([26,31,37,38,61,65,66,67,70,72,73,74,80,85,87,88,89,93,96,98,103,106,108,109,110,111,112,115,116,118,119,120,],[-32,-38,-49,-57,-40,-33,-56,-34,-39,-57,93,-56,-45,-50,-53,-36,-37,-58,-52,-35,112,-49,-49,115,-59,116,-51,-41,-43,-44,120,-42,]),'PUNTO':([29,33,104,],[68,71,113,]),'PROGRAM':([32,],[70,]),'NOW':([68,],[88,]),'LLDER':([69,],[89,]),'READKEY':([71,],[90,]),'WRITELINE':([71,],[91,]),'READLINE':([113,],[117,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'module':([0,],[1,]),'program':([0,],[2,]),'constDecl':([0,],[3,]),'empty':([0,3,6,11,21,59,],[5,8,12,25,25,25,]),'varDecl':([3,],[6,]),'constAssignmentList':([4,],[9,]),'procDecl':([6,],[11,]),'identList':([7,],[13,]),'statement':([11,21,59,],[18,60,84,]),'expression':([11,21,34,49,50,51,59,82,86,107,],[20,20,73,79,80,81,20,98,73,73,]),'condition':([11,21,59,],[23,23,23,]),'term':([11,21,27,28,34,49,50,51,52,59,76,82,86,99,100,107,114,],[26,26,65,67,26,26,26,26,82,26,96,26,26,67,65,26,118,]),'multiplyingOperator':([11,21,26,34,49,50,51,59,65,67,82,86,96,107,118,],[27,27,63,27,27,27,27,27,63,63,100,27,63,27,63,]),'addingOperator':([11,20,21,26,34,49,50,51,59,65,67,73,79,80,81,82,86,96,98,107,118,],[28,52,28,64,28,28,28,28,28,64,64,52,52,52,52,99,28,64,52,28,64,]),'factor':([11,21,27,28,34,49,50,51,52,59,63,64,76,82,86,99,100,107,114,],[37,37,37,37,37,37,37,37,37,37,85,87,37,37,37,106,108,37,37,]),'relation':([20,],[51,]),'statementList':([21,],[59,]),'boolean':([101,],[109,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> module","S'",1,None,None,None),
  ('module -> program','module',1,'p_module','analizadorSintacticoBasico.py',29),
  ('program -> constDecl varDecl procDecl statement','program',4,'p_program','analizadorSintacticoBasico.py',34),
  ('args -> ARGS','args',1,'p_args','analizadorSintacticoBasico.py',39),
  ('imports -> IMPORTS ID','imports',2,'p_imports','analizadorSintacticoBasico.py',42),
  ('constDecl -> DIM constAssignmentList','constDecl',2,'p_constDecl','analizadorSintacticoBasico.py',52),
  ('constDecl -> DIM ID IGUAL ID','constDecl',4,'p_constDecl1','analizadorSintacticoBasico.py',58),
  ('constDecl -> DIM ID AS ID IGUAL ID','constDecl',6,'p_constDecl2','analizadorSintacticoBasico.py',64),
  ('constDecl -> empty','constDecl',1,'p_constDeclEmpty','analizadorSintacticoBasico.py',70),
  ('constAssignmentList -> ID IGUAL NUMERO','constAssignmentList',3,'p_constAssignmentList1','analizadorSintacticoBasico.py',76),
  ('constAssignmentList -> constAssignmentList ID IGUAL NUMERO','constAssignmentList',4,'p_constAssignmentList2','analizadorSintacticoBasico.py',80),
  ('varDecl -> DIM identList','varDecl',2,'p_varDecl1','analizadorSintacticoBasico.py',84),
  ('varDecl -> empty','varDecl',1,'p_varDeclEmpty','analizadorSintacticoBasico.py',88),
  ('identList -> ID','identList',1,'p_identList1','analizadorSintacticoBasico.py',92),
  ('identList -> identList ID','identList',2,'p_identList2','analizadorSintacticoBasico.py',96),
  ('procDecl -> empty','procDecl',1,'p_procDeclEmpty','analizadorSintacticoBasico.py',104),
  ('statement -> ID UPDATE expression','statement',3,'p_statement1','analizadorSintacticoBasico.py',108),
  ('statement -> ID','statement',1,'p_statement2','analizadorSintacticoBasico.py',112),
  ('statement -> BEGIN statementList END','statement',3,'p_statement3','analizadorSintacticoBasico.py',116),
  ('statement -> condition','statement',1,'p_statement4','analizadorSintacticoBasico.py',120),
  ('statement -> IMPORTS ID','statement',2,'p_statement5','analizadorSintacticoBasico.py',124),
  ('statement -> empty','statement',1,'p_statementEmpty','analizadorSintacticoBasico.py',136),
  ('statementList -> statement','statementList',1,'p_statementList1','analizadorSintacticoBasico.py',140),
  ('statementList -> statementList statement','statementList',2,'p_statementList2','analizadorSintacticoBasico.py',144),
  ('condition -> expression','condition',1,'p_condition1','analizadorSintacticoBasico.py',148),
  ('condition -> expression relation expression','condition',3,'p_condition2','analizadorSintacticoBasico.py',152),
  ('relation -> IGUAL','relation',1,'p_relation1','analizadorSintacticoBasico.py',156),
  ('relation -> NOIGUAL','relation',1,'p_relation2','analizadorSintacticoBasico.py',160),
  ('relation -> MENORQ','relation',1,'p_relation3','analizadorSintacticoBasico.py',164),
  ('relation -> MAYORQ','relation',1,'p_relation4','analizadorSintacticoBasico.py',168),
  ('relation -> TRUE','relation',1,'p_relation5','analizadorSintacticoBasico.py',172),
  ('relation -> FALSE','relation',1,'p_relation6','analizadorSintacticoBasico.py',176),
  ('expression -> term','expression',1,'p_expression1','analizadorSintacticoBasico.py',180),
  ('expression -> multiplyingOperator term','expression',2,'p_expression2','analizadorSintacticoBasico.py',184),
  ('expression -> addingOperator term','expression',2,'p_expression3','analizadorSintacticoBasico.py',188),
  ('expression -> expression addingOperator term expression','expression',4,'p_expression14','analizadorSintacticoBasico.py',196),
  ('expression -> DATETIME PUNTO NOW','expression',3,'p_expression4','analizadorSintacticoBasico.py',204),
  ('expression -> LLIZQ ID LLDER','expression',3,'p_expression5','analizadorSintacticoBasico.py',208),
  ('expression -> VBCRLF','expression',1,'p_expression6','analizadorSintacticoBasico.py',212),
  ('expression -> MODULE PROGRAM','expression',2,'p_expression7','analizadorSintacticoBasico.py',217),
  ('expression -> END MODULE','expression',2,'p_expression8','analizadorSintacticoBasico.py',221),
  ('expression -> CONSOLE PUNTO READKEY PIZQ boolean PDER','expression',6,'p_expression9','analizadorSintacticoBasico.py',225),
  ('expression -> DIM ID IGUAL CONSOLE PUNTO READLINE PIZQ PDER','expression',8,'p_expression10','analizadorSintacticoBasico.py',229),
  ('expression -> CONSOLE PUNTO WRITELINE PIZQ ID PDER','expression',6,'p_expression11','analizadorSintacticoBasico.py',233),
  ('expression -> DIM ID AS BOOLEAN IGUAL term','expression',6,'p_expression12','analizadorSintacticoBasico.py',237),
  ('expression -> ID IGUAL expression','expression',3,'p_expression13','analizadorSintacticoBasico.py',241),
  ('addingOperator -> SUMA','addingOperator',1,'p_addingOperator1','analizadorSintacticoBasico.py',245),
  ('addingOperator -> RESTA','addingOperator',1,'p_addingOperator2','analizadorSintacticoBasico.py',249),
  ('addingOperator -> MOD','addingOperator',1,'p_addingOperator3','analizadorSintacticoBasico.py',253),
  ('term -> factor','term',1,'p_term1','analizadorSintacticoBasico.py',261),
  ('term -> term multiplyingOperator factor','term',3,'p_term2','analizadorSintacticoBasico.py',265),
  ('term -> PIZQ NUMERO MAYORQ NUMERO PDER','term',5,'p_term3','analizadorSintacticoBasico.py',269),
  ('term -> BOOLEAN IGUAL term','term',3,'p_term4','analizadorSintacticoBasico.py',273),
  ('term -> term addingOperator factor','term',3,'p_term5','analizadorSintacticoBasico.py',277),
  ('multiplyingOperator -> MULTI','multiplyingOperator',1,'p_multiplyingOperator1','analizadorSintacticoBasico.py',281),
  ('multiplyingOperator -> DIV','multiplyingOperator',1,'p_multiplyingOperator2','analizadorSintacticoBasico.py',285),
  ('factor -> ID','factor',1,'p_factor1','analizadorSintacticoBasico.py',289),
  ('factor -> NUMERO','factor',1,'p_factor2','analizadorSintacticoBasico.py',293),
  ('factor -> PIZQ expression PDER','factor',3,'p_factor3','analizadorSintacticoBasico.py',297),
  ('boolean -> BOOLEAN','boolean',1,'p_boolean','analizadorSintacticoBasico.py',304),
  ('empty -> <empty>','empty',0,'p_empty','analizadorSintacticoBasico.py',307),
]
