import ast
from functools import singledispatch

# Make built-in compile extensible (rename to `compiled` to avoid conflicts)
compiled = singledispatch(compile)


# Use of singledispatch is just an implementation detail (don't register other)
@singledispatch
def uneval(node):
    raise TypeError(f"Unsupported type: {type(node)}")


@uneval.register
def _(node: ast.AST):
    return node


@uneval.register(int)
@uneval.register(float)
@uneval.register(bool)
@uneval.register(bytes)
@uneval.register(bytearray)
@uneval.register(str)
@uneval.register(complex)
def _(node):
    return ast.Constant(node)


@uneval.register
def _(node: tuple):
    return ast.Tuple(elts=[uneval(x) for x in node], ctx=ast.Load())


@uneval.register
def _(node: list):
    return ast.List(elts=[uneval(x) for x in node], ctx=ast.Load())


@uneval.register
def _(node: set):
    return ast.Set(node)


@uneval.register
def _(node: dict):
    return ast.Dict(keys=[uneval(k) for k in node.keys()],
                    values=[uneval(v) for v in node.values()])


@uneval.register
def _(node: slice):
    return ast.Slice(uneval(node.start), uneval(node.stop), uneval(node.step))


@uneval.register
def _(node: range):
    args = [uneval(node.start), uneval(node.stop), uneval(node.step)]
    return ast.Call(ast.Name('range', ctx=ast.Load()), args=args, keywords=[])
