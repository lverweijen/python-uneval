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
