import ast
from types import CodeType
from typing import Any

from .expression import Expression
from .dsl import expr, ExprType


def compiled(obj: ExprType | CodeType, /) -> Any:
    """Compile the given expression.

    If expression is an Expression, the result is memoized.
    Similar to built-in function compile, but specialized for Expression and always sets `mode="eval"`.
    """
    match obj:
        case Expression():
            return obj._compile()
        case CodeType():
            return obj
        case str() | ast.AST():
            return expr(obj)._compile()
        case _:
            raise TypeError(f"{type(obj)} is not an Expression.")


def evaluate(obj: ExprType | CodeType, data=None, /, **kwargs) -> Any:
    """Evaluate the expression.

    Similar to built-in function eval, but specialized to work with Expression.
    """
    return eval(compiled(obj), kwargs, data)
