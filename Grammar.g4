grammar Grammar;

program
    : programElement* EOF
    ;

programElement
    : methodDeclaration
    | variableDeclaration
    ;

methodDeclaration
    : type Identifier formalParameters block
    ;

formalParameters
    : '(' formalParameterList? ')'
    ;

formalParameterList
    : formalParameter (',' formalParameter)*
    ;

formalParameter
    : type Identifier
    ;

block
    : '{' blockStatement* '}'
    ;

blockStatement
    : variableDeclaration
    | statement
    ;

statement
    : 'if' parExpression brackedStatement ('else' brackedStatement)?
    | 'while' parExpression brackedStatement
    | 'return' expression? ';'
    | statementExpression ';'
    ;

brackedStatement
    : '{' statement* '}'
    ;

parExpression
    : '(' expression ')'
    ;

statementExpression
    :   expression
    ;

variableDeclaration
    : type variableDeclarator ';'
    ;

type
    : 'boolean'
    | 'int'
    | 'long'
    ;

variableDeclarator
    : Identifier ('=' expression)?
    ;

Identifier
    : Letter LetterOrDigit*
    ;

expression
    : primary
    | expression '(' expressionList? ')'
    | ('+'|'-') expression
    | expression ('*'|'/'|'%') expression
    | expression ('+'|'-') expression
    | expression ('<' '<' | '>' '>' '>' | '>' '>') expression
    | expression ('<=' | '>=' | '>' | '<') expression
    | expression ('==' | '!=') expression
    | expression '&&' expression
    | expression '||' expression
    | <assoc=right> expression '=' expression
    ;

expressionList
    :   expression (',' expression)*
    ;

primary
    :   '(' expression ')'
    |   literal
    |   Identifier
    ;

literal
    : IntegerLiteral
    | BooleanLiteral
    ;

IntegerLiteral : Number NumberSuffix? ;
BooleanLiteral : 'true' | 'false' ;

fragment Number : '0' | NonZeroDigit Digit* ;
fragment NumberSuffix : [lL] ;
fragment Digit : '0' | NonZeroDigit ;
fragment NonZeroDigit : [1-9] ;

fragment Letter : [a-zA-Z_] ;
fragment LetterOrDigit : [a-zA-Z0-9_] ;

WS : [ \t\u000C\r\n]+ -> skip ;
COMMENT : '//' ~[\r\n]* -> skip ;
