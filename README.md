# UnEval #

UnEval is a microlibrary for generating python-expressions, which can be converted to runnable pythoncode.

Some use cases of this library are:
- Manipulation of the python-[abstract syntax tree](https://docs.python.org/3/library/ast.html).
- Writing [domain specific languages](https://en.wikipedia.org/wiki/Domain-specific_language).
- [Code generation](https://en.wikipedia.org/wiki/Macro).

I have the intention to build something on top of this later that converts python expressions to linear programming constraints.

## Usage ##

Firstly, the building blocks can be used to generate expressions.
Secondly, these expressions can be converted.

### Building blocks ###

| Factory       | AST-class             | Example                                         |
|---------------|-----------------------|-------------------------------------------------|
| `quote`       | `ast.Name`            | `quote('a')` or `quote.a` (shortcut)            |
| `if_`         | `ast.IfExpr`          | `if_(quote.x >= 0, quote.x, -quote.x)`          |
| `for_`        | `ast.GenExpr`         | `for_(quote.x ** 2, (quote.x, quote.range(5)))` |
| `lambda_`     | `ast.Lambda`          | `lambda_([quote.x], quote.x * quote.x)`         |
| `and_`, `or_` | `ast.BoolOp`          | `and_(quote.x >= 10, quote.x <= 15)`            |
| `not_`, `in_` | `ast.Not(), ast.In()` | `not_(in_(quote.x, {1, 2, 3}))`                 |

### Converters ###

| Converter       | Target      | Remark                     |
|-----------------|-------------|----------------------------|
| `str`           | String      | Convert to readable python |
| `to_expression` | Expression  | Parse existing string      |
| `to_ast`        | AST-node    | Generates AST-node         |
| `to_code`       | Code-object | Compiles the expression    |                    

### Examples ###

```python
# Create variables
x, y = quote.x, quote.y  # Shortcut for quote("x"), quote("y")

# Manipulate
z = x*x + y*y
d = z.abs() + x.pow(3) - y.sin(x)

# Convert
print(z)  # x * x + y * y
print(ast.dump(to_ast(z)))  # BinOp(left=BinOp(left=Name(id='x', ctx=Load()), op=Mult(), right=Name(id='x', ctx=Load())), op=Add(), right=BinOp(left=Name(id='y', ctx=Load()), op=Mult(), right=Name(id='y', ctx=Load())))
print(eval(to_code(z), {"x": 3, "y": 4}))  # 25
```

These ideas can be used to create alternative syntax for [lambda](https://docs.python.org/3/reference/expressions.html#lambda)-functions:

```python
from uneval import Expression, to_code, lambda_, quote

x = quote.x

def f_x(expr: Expression):
  """Create a lambda with parameter x."""
  return eval(to_code(lambda_([x], expr)))

square = f_x(x * x)  # Same as lambda x: x * x
print(square(5))  # => 25
```

You can also use it with [pandas](https://pandas.pydata.org/) in combination with [eval](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.eval.html#pandas.DataFrame.eval) and [query](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.query.html#pandas.DataFrame.query):

```python
from uneval import quote as q

# No syntax highlighting.
df.eval("bmi = mass / height**2")

# With syntax highlighting
df.eval(f"bmi = {q.mass / q.height**2}")
```

## Similar work ##

Libraries that implement something similar:
- [Macropy](https://github.com/lihaoyi/macropy) has [quasiquote](https://macropy3.readthedocs.io/en/latest/reference.html#quasiquote).
- [Polars](https://docs.pola.rs/user-guide/expressions/) - Writing `col.x` creates something like this `Expression`-object.
- [SymPy](https://www.sympy.org/en/index.html) - Symbolic manipulation, but its representation is different from Python.
- [pulp](https://github.com/coin-or/pulp) - Can build objectives and constraints for solving linear programming problems.
- [sqlalchemy](https://www.sqlalchemy.org/) - Generates properties based on a schema.
- [latexify](https://github.com/google/latexify_py) - Converts python to SQL.

Other:
- [Fixing lambda](https://stupidpythonideas.blogspot.com/2014/02/fixing-lambda.html) - A blog post about alternative lambda syntaxes.
- [Mini-lambda](https://smarie.github.io/python-mini-lambda/#see-also) - Packages to "fix" lambda.
- [Meta](https://srossross.github.io/Meta/html/) - A few utils to work on AST's.
- [python macros use cases](https://stackoverflow.com/questions/764412/python-macros-use-cases) - Stack-overflow discussion.

Useful references:
- [Green tree snakes](https://greentreesnakes.readthedocs.io/en/latest/)
