### syntax:
```
script: EPS | stmt SEMI script
stmt: KW_CONNECT KW_TO STRING | KW_LIST | select_stmt | named_pattern
named_pattern: NT_NAME OP_EQ pattern
select_stmt: KW_SELECT obj_expr KW_FROM STRING KW_WHERE where_expr
obj_expr: vs_info | KW_COUNT vs_info | KW_EXISTS vs_info
vs_info: LBR v_info COMMA v_info RBR | v_info
v_info: SYMB | UNDERSCORE
where_expr: LBR v_expr RBR OP_MINUS pattern OP_MINUS OP_GR LBR v_expr RBR
v_expr: SYMB | UNDERSCORE | SYMB DOT KW_ID OP_EQ INT
pattern: elem | elem MID pattern
elem: seq | LBR RBR
seq: seq_elem | seq_elem seq
seq_elem: prim_pattern | prim_pattern OP_STAR | prim_pattern OP_PLUS | prim_pattern OP_Q
prim_pattern: SYMB | NT_NAME | LBR pattern RBR
```
### tokens (terminals):
```
LBR = "("
RBR = ")"
COMMA = ","
SEMI = ";"
MID = "|"
DOT = "."
UNDERSCORE = "_"
EPS = ""
OP_STAR = "*"
OP_PLUS = "+"
OP_Q = "?"
OP_MINUS = "-"
OP_GR = ">"
OP_EQ = "="
KW_ID = "id"
KW_COUNT = "count"
KW_EXISTS = "exists"
KW_FROM = "from"
KW_WHERE = "where"
KW_LIST = "list"
KW_CONNECT = "connect"
KW_TO = "to"
SYMB = [a − z][a − z]*
INT = 0 | [1 − 9][0 − 9]∗
NT_NAME = [A − Z][a − z]*
STRING = "["([aA − zZ] | [0 − 9] | ("-"| " " | "_" | "/" | "."))*"]"
```
### examples:

#### patterns:
```
a S (a | b)?
() | (a S)*
```
#### named patterns:
```
S = a S b | ()
A = (a)*
```
#### select statements:
```
select count (v, u) from [graph1.txt] where (u.id = 2) - (a | b)* -> (v.id = 3)
select exists u from [graph2.txt] where (u) - S -> (v.id = 1)
```
#### script:
```
connect to [\home\user\graph_db];
S = a S b S | ();
select count u from [graph.txt] where (v.id = 1) - S -> (u);
```

