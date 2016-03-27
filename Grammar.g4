grammar Grammar;

@header {
from entity.Program import Program
from entity.Variable import Variable
from entity.Function import *
from entity.Expression import *
from entity.Type import Type
from entity.Scalar import *
from entity.Statement import *
}

@parser::members {
    self.program_states = Program()
}

program
    : (programElement{self.program_states.add($programElement.element)})* EOF
    ;

programElement returns [element = None]
    : functionDeclaration
    {$element = $functionDeclaration.function}
    | variableDeclaration
    {$element = $variableDeclaration.variable}
    ;

functionDeclaration returns [function = None]
    : valueType Identifier formalParameters block
    {$function = Function($valueType.value_type, $Identifier.text, $formalParameters.params, $block.statements)}
    ;

formalParameters returns [params = None]
    : '(' (formalParameterList{$params = $formalParameterList.params})? ')'
    ;

formalParameterList returns [params = None]
    @init {$params = []}
    : formalParameter{$params.append($formalParameter.variable)}
        (',' formalParameter{$params.append($formalParameter.variable)})*
    ;

formalParameter returns [variable = None]
    : valueType Identifier
    {$variable = Variable($valueType.value_type, $Identifier.text, CallFunctionStatement("_pop"))}
    ;

block returns [statements = None]
    @init {$statements = []}
    : '{' (blockStatement{$statements.append($blockStatement.state)})* '}'
    ;

blockStatement returns [state = None]
    : variableDeclaration
    {$state = $variableDeclaration.variable}
    | statement
    {$state = $statement.state}
    ;

statement returns [state = None]
    @init{tmp_var = None}
    : 'if' parExpression brackedStatement
        ('else' brackedStatement{tmp_var = ElseStatement($brackedStatement.statements)})?
    {$state = IfStatement($parExpression.expr, $brackedStatement.statements, tmp_var)}
    | 'while' parExpression brackedStatement
    {$state = WhileStatement($parExpression.expr, $brackedStatement.statements)}
    | 'return' (expression{tmp_var = $expression.expr})? ';'
    {$state = ReturnStatement(tmp_var)}
    | callFunction ';'
    {$state = $callFunction.expr}
    ;

brackedStatement returns [statements = None]
    @init{$statements = []}
    : '{' (blockStatement{$statements.append($blockStatement.state)})* '}'
    ;

parExpression returns [expr = None]
    : '(' expression ')'
    {$expr = $expression.expr}
    ;

callFunction returns [expr = None]
    : expression
    {$expr = $expression.expr}
    ;

variableDeclaration returns [variable = None]
    : valueType variableDeclarator ';'
    {$variable = Variable($valueType.value_type, $variableDeclarator.name_value[0], $variableDeclarator.name_value[1])}
    ;

valueType returns [value_type = None]
    : 'boolean'
    {$value_type = Type.boolean}
    | 'int'
    {$value_type = Type.int}
    ;

variableDeclarator returns [name_value = None]
    @init{expr = None}
    : Identifier ('=' expression{expr = $expression.expr})?
    {$name_value = ($Identifier.text, expr)}
    ;

expression returns [expr = None]
    @init{tmp_var = None}
    : primary
    {$expr = $primary.expr}
    | e=expression '(' (expressionList{tmp_var = $expressionList.args})? ')'
    {$expr = CallFunctionStatement($e.text, tmp_var)}
    | sign=('+'|'-') expression
    {$expr = get_expression($sign.text, None, $expression.expr)}
    | e1=expression sign=('*'|'/'|'%') e2=expression
    {$expr = get_expression($sign.text, $e1.expr, $e2.expr)}
    | e1=expression sign=('+'|'-') e2=expression
    {$expr = get_expression($sign.text, $e1.expr, $e2.expr)}
    | e1=expression sign=('<=' | '>=' | '>' | '<') e2=expression
    {$expr = get_expression($sign.text, $e1.expr, $e2.expr)}
    | e1=expression sign=('==' | '!=') e2=expression
    {$expr = get_expression($sign.text, $e1.expr, $e2.expr)}
    | e1=expression sign='&&' e2=expression
    {$expr = get_expression($sign.text, $e1.expr, $e2.expr)}
    | e1=expression sign='||' e2=expression
    {$expr = get_expression($sign.text, $e1.expr, $e2.expr)}
    | <assoc=right> n=expression '=' e=expression
    {$expr = AssignmentOperator($n.expr, $e.expr)}
    ;

expressionList returns [args = None]
    @init{$args = []}
    : expression{$args.append($expression.expr)} (',' expression{$args.append($expression.expr)})*
    ;

primary returns [expr = None]
    : '(' expression ')'
    {$expr = $expression.expr}
    | literal
    {$expr = get_scalar($literal.text)}
    | Identifier
    {$expr = get_scalar($Identifier.text)}
    ;

Identifier
    : Letter LetterOrDigit*
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

fragment Letter : [a-zA-Z] ;
fragment LetterOrDigit : [a-zA-Z0-9_] ;

WS : [ \t\u000C\r\n]+ -> skip ;
COMMENT : '//' ~[\r\n]* -> skip ;
