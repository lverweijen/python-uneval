import ast
from collections.abc import Hashable
from functools import singledispatch

# Make built-in compile extensible
compile = compile_ = singledispatch(compile)


# Use of singledispatch is just an implementation detail (don't register other)
@singledispatch
def to_ast(node):
    raise TypeError(f"Unsupported type: {type(node)}")


@to_ast.register
def _(node: ast.AST):
    return node


@to_ast.register
def _(node: Hashable):
    return ast.Constant(node)


@to_ast.register
def _(node: tuple):
    return ast.Tuple(elts=[to_ast(x) for x in node], ctx=ast.Load())


@to_ast.register
def _(node: list):
    return ast.List(elts=[to_ast(x) for x in node], ctx=ast.Load())


@to_ast.register
def _(node: set):
    return ast.Set(node)


@to_ast.register
def _(node: dict):
    return ast.Dict(keys=[to_ast(k) for k in node.keys()],
                    values=[to_ast(v) for v in node.values()])


@to_ast.register
def _(node: slice):
    return ast.Slice(to_ast(node.start), to_ast(node.stop), to_ast(node.step))


@to_ast.register
def _(node: range):
    args = [to_ast(node.start), to_ast(node.stop), to_ast(node.step)]
    return ast.Call(ast.Name('range', ctx=ast.Load()), args=args, keywords=[])
