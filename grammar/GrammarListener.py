# Generated from /home/isamborskiy/Python/Compiler/grammar/Grammar.g4 by ANTLR 4.5.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .GrammarParser import GrammarParser
else:
    from GrammarParser import GrammarParser

from entity.Program import Program
from entity.Variable import Variable
from entity.Function import *
from entity.Expression import *
from entity.Type import Type
from entity.Array import *
from entity.Scalar import *
from entity.Statement import *


# This class defines a complete listener for a parse tree produced by GrammarParser.
class GrammarListener(ParseTreeListener):

    # Enter a parse tree produced by GrammarParser#program.
    def enterProgram(self, ctx:GrammarParser.ProgramContext):
        pass

    # Exit a parse tree produced by GrammarParser#program.
    def exitProgram(self, ctx:GrammarParser.ProgramContext):
        pass


    # Enter a parse tree produced by GrammarParser#programElement.
    def enterProgramElement(self, ctx:GrammarParser.ProgramElementContext):
        pass

    # Exit a parse tree produced by GrammarParser#programElement.
    def exitProgramElement(self, ctx:GrammarParser.ProgramElementContext):
        pass


    # Enter a parse tree produced by GrammarParser#functionDeclaration.
    def enterFunctionDeclaration(self, ctx:GrammarParser.FunctionDeclarationContext):
        pass

    # Exit a parse tree produced by GrammarParser#functionDeclaration.
    def exitFunctionDeclaration(self, ctx:GrammarParser.FunctionDeclarationContext):
        pass


    # Enter a parse tree produced by GrammarParser#formalParameters.
    def enterFormalParameters(self, ctx:GrammarParser.FormalParametersContext):
        pass

    # Exit a parse tree produced by GrammarParser#formalParameters.
    def exitFormalParameters(self, ctx:GrammarParser.FormalParametersContext):
        pass


    # Enter a parse tree produced by GrammarParser#formalParameterList.
    def enterFormalParameterList(self, ctx:GrammarParser.FormalParameterListContext):
        pass

    # Exit a parse tree produced by GrammarParser#formalParameterList.
    def exitFormalParameterList(self, ctx:GrammarParser.FormalParameterListContext):
        pass


    # Enter a parse tree produced by GrammarParser#formalParameter.
    def enterFormalParameter(self, ctx:GrammarParser.FormalParameterContext):
        pass

    # Exit a parse tree produced by GrammarParser#formalParameter.
    def exitFormalParameter(self, ctx:GrammarParser.FormalParameterContext):
        pass


    # Enter a parse tree produced by GrammarParser#block.
    def enterBlock(self, ctx:GrammarParser.BlockContext):
        pass

    # Exit a parse tree produced by GrammarParser#block.
    def exitBlock(self, ctx:GrammarParser.BlockContext):
        pass


    # Enter a parse tree produced by GrammarParser#blockStatement.
    def enterBlockStatement(self, ctx:GrammarParser.BlockStatementContext):
        pass

    # Exit a parse tree produced by GrammarParser#blockStatement.
    def exitBlockStatement(self, ctx:GrammarParser.BlockStatementContext):
        pass


    # Enter a parse tree produced by GrammarParser#statement.
    def enterStatement(self, ctx:GrammarParser.StatementContext):
        pass

    # Exit a parse tree produced by GrammarParser#statement.
    def exitStatement(self, ctx:GrammarParser.StatementContext):
        pass


    # Enter a parse tree produced by GrammarParser#brackedStatement.
    def enterBrackedStatement(self, ctx:GrammarParser.BrackedStatementContext):
        pass

    # Exit a parse tree produced by GrammarParser#brackedStatement.
    def exitBrackedStatement(self, ctx:GrammarParser.BrackedStatementContext):
        pass


    # Enter a parse tree produced by GrammarParser#parExpression.
    def enterParExpression(self, ctx:GrammarParser.ParExpressionContext):
        pass

    # Exit a parse tree produced by GrammarParser#parExpression.
    def exitParExpression(self, ctx:GrammarParser.ParExpressionContext):
        pass


    # Enter a parse tree produced by GrammarParser#callFunction.
    def enterCallFunction(self, ctx:GrammarParser.CallFunctionContext):
        pass

    # Exit a parse tree produced by GrammarParser#callFunction.
    def exitCallFunction(self, ctx:GrammarParser.CallFunctionContext):
        pass


    # Enter a parse tree produced by GrammarParser#variableDeclaration.
    def enterVariableDeclaration(self, ctx:GrammarParser.VariableDeclarationContext):
        pass

    # Exit a parse tree produced by GrammarParser#variableDeclaration.
    def exitVariableDeclaration(self, ctx:GrammarParser.VariableDeclarationContext):
        pass


    # Enter a parse tree produced by GrammarParser#valueType.
    def enterValueType(self, ctx:GrammarParser.ValueTypeContext):
        pass

    # Exit a parse tree produced by GrammarParser#valueType.
    def exitValueType(self, ctx:GrammarParser.ValueTypeContext):
        pass


    # Enter a parse tree produced by GrammarParser#primitiveType.
    def enterPrimitiveType(self, ctx:GrammarParser.PrimitiveTypeContext):
        pass

    # Exit a parse tree produced by GrammarParser#primitiveType.
    def exitPrimitiveType(self, ctx:GrammarParser.PrimitiveTypeContext):
        pass


    # Enter a parse tree produced by GrammarParser#variableDeclarator.
    def enterVariableDeclarator(self, ctx:GrammarParser.VariableDeclaratorContext):
        pass

    # Exit a parse tree produced by GrammarParser#variableDeclarator.
    def exitVariableDeclarator(self, ctx:GrammarParser.VariableDeclaratorContext):
        pass


    # Enter a parse tree produced by GrammarParser#expression.
    def enterExpression(self, ctx:GrammarParser.ExpressionContext):
        pass

    # Exit a parse tree produced by GrammarParser#expression.
    def exitExpression(self, ctx:GrammarParser.ExpressionContext):
        pass


    # Enter a parse tree produced by GrammarParser#expressionList.
    def enterExpressionList(self, ctx:GrammarParser.ExpressionListContext):
        pass

    # Exit a parse tree produced by GrammarParser#expressionList.
    def exitExpressionList(self, ctx:GrammarParser.ExpressionListContext):
        pass


    # Enter a parse tree produced by GrammarParser#creator.
    def enterCreator(self, ctx:GrammarParser.CreatorContext):
        pass

    # Exit a parse tree produced by GrammarParser#creator.
    def exitCreator(self, ctx:GrammarParser.CreatorContext):
        pass


    # Enter a parse tree produced by GrammarParser#primary.
    def enterPrimary(self, ctx:GrammarParser.PrimaryContext):
        pass

    # Exit a parse tree produced by GrammarParser#primary.
    def exitPrimary(self, ctx:GrammarParser.PrimaryContext):
        pass


    # Enter a parse tree produced by GrammarParser#literal.
    def enterLiteral(self, ctx:GrammarParser.LiteralContext):
        pass

    # Exit a parse tree produced by GrammarParser#literal.
    def exitLiteral(self, ctx:GrammarParser.LiteralContext):
        pass


