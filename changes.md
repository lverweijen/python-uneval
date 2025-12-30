# 0.2.0

- New factory function `expr` to convert `str` or `AST` to expression.
- New factory function `scoped` to capture an expression with context.
- New function `evaluate` to evaluate on Expression.
- New function `lit` to explicitly convert a literal value to an Expression.
- New function `compiled` to compile an expression.
- Remove function `to_bytecode`. It has been replaced by `compiled`.
- Rename function/dsl `quote` to `var`.
- The constructor of `Expression` has been simplified and only works with `AST`. Use `expr` if a flexible constructor is needed.
- The functions `eval` and `F` now ignore surrounding context, unless the expression is wrapped by `scoped`.
- The functions `eval` and `F` can now be passed additional arguments that augment the evaluation scope.

Differences between `compiled` and `to_bytecode`:
- If `compiled` is passed a string it is now interpreted as an expression, whereas `to_bytecode` interpreted it as a value.
- If `compiled` is passed an `Expression`, the result is now cached.

# 0.1.2

- Fix `or_` function.

# 0.1.1

- Support `to_ast(None)`
- Disallow `iter(expression)`. Use `quote.iter(expression)` instead.
- Disallow `expression._generic_()`. Use `quote.generic(expression)` instead.

# 0.1.0

- Rename `to_code` to `to_bytecode`.
- Whitelist literals (constants) instead of using Hashable.
  This makes binary operators operands fail earlier that would have failed anyway.
- Make binary operators return `NotImplemented` when working with unknown datatypes.
- Support `to_ast(frozenset())`.
