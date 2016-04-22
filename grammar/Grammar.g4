grammar Grammar;

@header {
from entity.Program import Program
from entity.Variable import Variable
from entity.Function import *
from entity.Expression import *
from entity.Type import Type
from entity.Array import *
from entity.Scalar import *
from entity.Statement import *
}

@parser::members {
    self.program_states = Program()

def append_to_array(self, array, element):
    if array is None:
        return [element]
    else:
        array.append(element)
        return array
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
    {$function = get_function($valueType.value_type, $Identifier.text, $formalParameters.params, $block.statements)}
    | 'void' Identifier formalParameters block
    {$function = get_function(None, $Identifier.text, $formalParameters.params, $block.statements)}
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
    {$variable = Variable($valueType.value_type, $Identifier.text)}
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
    @init {tmp_var = None}
    : 'if' parExpression b1=brackedStatement
        ('else' b2=brackedStatement{tmp_var = ElseStatement($b2.statements)})?
    {$state = IfStatement($parExpression.expr, $b1.statements, tmp_var)}
    | 'while' parExpression b1=brackedStatement
    {$state = WhileStatement($parExpression.expr, $b1.statements)}
    | 'return' (expression{tmp_var = $expression.expr})? ';'
    {$state = ReturnStatement(tmp_var)}
    | callFunction ';'
    {$state = $callFunction.expr}
    ;

brackedStatement returns [statements = None]
    @init {$statements = []}
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
    @init {dimension = 0}
    : primitiveType (('[' ']'){dimension += 1})*
    {$value_type = $primitiveType.value_type if dimension == 0 else Array($primitiveType.value_type, dimension)}
    ;

primitiveType returns [value_type = None]
    : 'boolean'
    {$value_type = Type.boolean}
    | 'int'
    {$value_type = Type.int}
    | 'char'
    {$value_type = Type.char}
    ;

variableDeclarator returns [name_value = None]
    : Identifier '=' expression
    {$name_value = ($Identifier.text, $expression.expr)}
    ;

expression returns [expr = None]
    @init {tmp_var = None}
    : primary
    {$expr = $primary.expr}
    | e1=expression ('[' e2=expression{tmp_var = self.append_to_array(tmp_var, $e2.expr)} ']')+
    {$expr = ArrayGetter($e1.expr, tmp_var)}
    | e=expression '(' (expressionList{tmp_var = $expressionList.args})? ')'
    {$expr = get_call_function_statement($e.text, tmp_var)}
    | 'new' creator
    {$expr = $creator.constr}
    | sign=('+'|'-') e=expression
    {$expr = get_expression($sign.text, None, $e.expr)}
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
    @init {$args = []}
    : expression{$args.append($expression.expr)} (',' expression{$args.append($expression.expr)})*
    ;

creator returns [constr = None]
    @init {dimensions_sizes = []}
    : primitiveType ('[' expression{dimensions_sizes.append($expression.expr)} ']')+
    {$constr = ArrayCreator($primitiveType.value_type, dimensions_sizes)}
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
    | CharacterLiteral
    | StringLiteral
    ;

IntegerLiteral : Number ;
BooleanLiteral : 'true' | 'false' ;
CharacterLiteral
    :   '\'' SingleCharacter '\''
    |   '\'' EscapeSequence '\''
    ;

fragment
SingleCharacter
    :   ~['\\]
    ;


StringLiteral
    :   '"' StringCharacters? '"'
    ;

fragment
StringCharacters
    :   StringCharacter+
    ;

fragment
StringCharacter
    :   ~["\\]
    |   EscapeSequence
    ;

fragment
EscapeSequence
    :   '\\' [btnfr"'\\]
    ;

fragment Number : '0' | NonZeroDigit Digit* ;
fragment Digit : '0' | NonZeroDigit ;
fragment NonZeroDigit : [1-9] ;

fragment Letter : [a-zA-Z] ;
fragment LetterOrDigit : [a-zA-Z0-9_] ;

WS : [ \t\u000C\r\n]+ -> skip ;
COMMENT : '//' ~[\r\n]* -> skip ;
