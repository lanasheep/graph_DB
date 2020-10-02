### syntax:
```
script: EPS | stmt SEMI script
stmt: KW_CONNECT KW_TO STRING | KW_LIST KW_ALL? STRING? | select_stmt | named_pattern
named_pattern: NT_NAME OP_EQ pattern
select_stmt: KW_SELECT func KW_FROM STRING KW_WHERE where_expr
func: KW_GET | KW_COUNT | KW_EXISTS 
where_expr: LBR v_expr RBR OP_MINUS pattern OP_MINUS OP_GR LBR v_expr RBR
v_expr: INT | UNDERSCORE 
pattern: elem | elem MID pattern
elem: seq | LBR RBR
seq: seq_elem | seq_elem seq
seq_elem: prim_pattern | prim_pattern OP_STAR 
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
OP_MINUS = "-"
OP_GR = ">"
OP_EQ = "="
KW_SELECT = "select"
KW_GET = "get"
KW_COUNT = "count"
KW_EXISTS = "exists"
KW_FROM = "from"
KW_WHERE = "where"
KW_LIST = "list"
KW_ALL : 'all' ;
KW_CONNECT = "connect"
KW_TO = "to"
SYMB = [a − z][a − z]*
INT = 0 | [1 − 9][0 − 9]*
NT_NAME = [A − Z]+
STRING = "["([aA − zZ] | [0 − 9] | ("\\" | "-"| " " | "_" | "/" | "." | "," | ":"))*"]"
```
### examples:

#### patterns
```
a S (a | b)*
() | (a S)*
```
#### named patterns
```
S = a S b | ()
A = (a)*
```
#### connect
```
connect to [\home\user\graph_db]
```
#### list

######by default displays graphs from the connected database if no path is specified
```
list all
list all [\home\user\another_graph_db]
```
######print set of different edge labels in the specified graph
```
list [\home\user\agraph_db\graph1.txt]
```
#### select statements

######it is possible to specify the vertex number or write underscore instead (vertex with any number)
###### getting all pairs of vertices that match the conditions:
```
select get from [graph1.txt] where (_) - (a | b)* -> (_)
```
###### finding the number of pairs of vertices that match the conditions:
```
select count from [graph1.txt] where (2) - (a | b)* -> (_)
```
###### checking for the existence of a pair of vertices that match the conditions:
```
select exists from [graph1.txt] where (1) - S -> (3)
```
#### script
```
connect to [\home\user\graph_db];
S = a S b S | ();
select count from [graph.txt] where (_) - S -> (1);
```

