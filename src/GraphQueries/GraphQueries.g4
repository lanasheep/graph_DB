grammar GraphQueries;

script : (stmt SEMI)* EOF ;

stmt : KW_CONNECT KW_TO STRING
     | KW_LIST
     | select_stmt
     | named_pattern
     ;

named_pattern : NT_NAME OP_EQ pattern ;

select_stmt : KW_SELECT obj_expr KW_FROM STRING KW_WHERE where_expr ;

obj_expr : vs_info
         | KW_COUNT vs_info
         | KW_EXISTS vs_info
         ;

vs_info : LBR v_info COMMA v_info RBR
        | v_info
        ;

v_info : SYMB
       | UNDERSCORE
       ;

where_expr : LBR v_expr RBR OP_MINUS pattern OP_MINUS OP_GR LBR v_expr RBR ;

v_expr : SYMB
       | UNDERSCORE
       | SYMB DOT KW_ID OP_EQ INT
       ;

pattern : elem
        | elem MID pattern
        ;

elem : seq
     | LBR RBR
     ;

seq : seq_elem
    | seq_elem seq
    ;

seq_elem : prim_pattern
         | prim_pattern OP_STAR
         | prim_pattern OP_PLUS
         | prim_pattern OP_Q
         ;

prim_pattern : SYMB
             | NT_NAME
             | LBR pattern RBR
             ;

LBR : '(' ;
RBR : ')' ;
COMMA : ',' ;
SEMI : ';' ;
MID : '|' ;
DOT : '.' ;
UNDERSCORE : '_' ;
OP_STAR : '*' ;
OP_PLUS : '+' ;
OP_Q : '?' ;
OP_MINUS : '-' ;
OP_GR : '>' ;
OP_EQ : '=' ;
KW_ID : 'id' ;
KW_SELECT : 'select' ;
KW_COUNT : 'count' ;
KW_EXISTS : 'exists' ;
KW_FROM : 'from' ;
KW_WHERE : 'where' ;
KW_LIST : 'list' ;
KW_CONNECT : 'connect' ;
KW_TO : 'to' ;
INT : '0'
    | [1−9][0−9]*
    ;
SYMB : [a-z]+ ;
NT_NAME : [A-Z]+ ;
STRING : '[' ([a-zA-Z]|[0-9]|('\\' | '-' | '_' | ' ' | '/' | '.' | ',' | ':'))* ']' ;
WS : [ \r\n\t]+ -> skip ;
