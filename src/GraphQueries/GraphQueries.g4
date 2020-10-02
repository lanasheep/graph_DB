grammar GraphQueries;

script : (stmt SEMI)* EOF ;

stmt : KW_CONNECT KW_TO STRING
     | KW_LIST
     | select_stmt
     | named_pattern
     ;

named_pattern : NT_NAME OP_EQ pattern ;

select_stmt : KW_SELECT func KW_FROM STRING KW_WHERE where_expr ;

func : KW_GET
     | KW_COUNT
     | KW_EXISTS
     ;

where_expr : LBR v_expr RBR OP_MINUS pattern OP_MINUS OP_GR LBR v_expr RBR ;

v_expr : INT
       | UNDERSCORE
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
OP_MINUS : '-' ;
OP_GR : '>' ;
OP_EQ : '=' ;
KW_SELECT : 'select' ;
KW_GET : 'get' ;
KW_COUNT : 'count' ;
KW_EXISTS : 'exists' ;
KW_FROM : 'from' ;
KW_WHERE : 'where' ;
KW_LIST : 'list' ;
KW_CONNECT : 'connect' ;
KW_TO : 'to' ;
INT : '0'
    | [1-9][0-9]*
    ;
SYMB : [a-z]+ ;
NT_NAME : [A-Z]+ ;
STRING : '[' ([a-zA-Z]|[0-9]|('\\' | '-' | '_' | ' ' | '/' | '.' | ',' | ':'))* ']' ;
WS : [ \r\n\t]+ -> skip ;
