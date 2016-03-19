grammar Grammar;
program
    : programElement*
    ;

programElement
    : variable
//    | function
//    | comment
    ;

variable
    : type NAME (ASSIGN value)
    ;

type
    : INT
    | LONG
    | BOOL
    ;

value
    : NUMBER
    | booleanLiteral
    ;

booleanLiteral
    : TRUE
    | FALSE
    ;

ASSIGN : '=' ;

INT  : 'int' ;
LONG : 'long' ;
BOOL : 'boolean' ;

TRUE  : 'true' ;
FALSE : 'false' ;

NUMBER       : '-'? NUM ;
fragment NUM : '0' | [1-9] [0-9]* ;

NAME : [a-fA-F] [0-9a-fA-F]* ;

WS : [ \t\u000C\r\n]+ -> skip ;
