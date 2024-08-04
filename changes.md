# 0.1.0

- Rename `to_code` to `to_bytecode`.
- Whitelist literals (constants) instead of using Hashable.
  This makes binary operators operands fail earlier that would have failed anyway.
- Make binary operators return `NotImplemented` when working with unknown datatypes.
- Support `to_ast(frozenset())`.
