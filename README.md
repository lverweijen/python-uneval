# UnEval #

UnEval is a microlibrary for generating python-expressions.

If you ever need to use
[eval](https://docs.python.org/3/library/functions.html#eval),
write [macros](https://en.wikipedia.org/wiki/Macro)
or implement [domain specific languages](https://en.wikipedia.org/wiki/Domain-specific_language),
this library provides a better way to generate python expressions than using [strings](https://docs.python.org/3/library/stdtypes.html#str).
Strings can contain syntax errors, make it harder to deal with parentheses and aren't syntax highlighted.
Expressions look and act a lot like pythoncode, except that they aren't evaluated immediately.

## Installation ##

Make sure to [install pip](https://pip.pypa.io/en/stable/installation/) then run:
```sh
pip install uneval
```

## Usage ##

Firstly, the building blocks can be used to generate expressions.
Secondly, these expressions can be converted.

### Examples ###

```python
# Build expressions
x, y = quote.x, quote.y  # Shortcut for quote("x"), quote("y")
z = x*x + y*y
d = z.abs() + x.pow(3) - y.sin(x)

# Convert
print(z)  # x * x + y * y
print(ast.dump(to_ast(z)))  # BinOp(left=BinOp(left=Name(id='x', ctx=Load()), op=Mult(), right=Name(id='x', ctx=Load())), op=Add(), right=BinOp(left=Name(id='y', ctx=Load()), op=Mult(), right=Name(id='y', ctx=Load())))
print(eval(to_code(z), {"x": 3, "y": 4}))  # 25
```

This can be used when working in [pandas](https://pandas.pydata.org/) and you want to use [eval](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.eval.html#pandas.DataFrame.eval) or [query](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.query.html#pandas.DataFrame.query):

```python
from uneval import quote as q

# No syntax highlighting. Syntax checkers won't catch errors.
df.eval("bmi = mass / height**2")

# With syntax highlighting. Syntax checkers can catch errors here.
df.eval(f"bmi = {q.mass / q.height**2}")
```

Expressions can also be converted to [λ](https://docs.python.org/3/glossary.html#term-lambda)-functions:

```python
from uneval import F, quote

x, y = quote.x, quote.y

hello = F("Hello World!")
hello()  # => "Hello World!"

plus1 = F.x(x + 1)
plus1(4)  # => 5

multiply = F.xy(x * y)
multiply(5, 7)  # => 35
```

### Building blocks ###

| Factory       | AST-class             | Example                                         | Result                     |
|---------------|-----------------------|-------------------------------------------------|----------------------------|
| `quote`       | `ast.Name`            | `quote('a')` or `quote.a` (shortcut)            | `a`                        |
| `if_`         | `ast.IfExpr`          | `if_(quote.x >= 0, quote.x, -quote.x)`          | `x if x >= 0 else -x`      |
| `for_`        | `ast.GenExpr`         | `for_(quote.x ** 2, (quote.x, quote.range(5)))` | `(x**2 for x in range(5))` |
| `lambda_`     | `ast.Lambda`          | `lambda_([quote.x], quote.x * quote.x)`         | `lambda x: x * x`          |
| `and_`, `or_` | `ast.BoolOp`          | `and_(quote.x >= 10, quote.x <= 15)`            | `x >= 10 and x <= 15`      |
| `not_`, `in_` | `ast.Not(), ast.In()` | `not_(in_(quote.x, {1, 2, 3}))`                 | `not x in {1, 2, 3}`       |

### Converters ###

| Converter    | Target      | Remark                     |
|--------------|-------------|----------------------------|
| `str`        | String      | Convert to readable python |
| `to_ast`     | AST-node    | Convert to AST-node        |
| `to_code`    | Code-object | Compile the expression     |
| `F.(params)` | Function    | Create a λ-function        |


## Similar work ##

Libraries that implement something similar:
- [Macropy](https://github.com/lihaoyi/macropy) has [quasiquote](https://macropy3.readthedocs.io/en/latest/reference.html#quasiquote).
- [SymPy](https://www.sympy.org/en/index.html) - Symbolic manipulation, but its representation is different from Python.
- [Polars](https://docs.pola.rs/user-guide/expressions/) - Writing `col.x` creates something like this `Expression`-object.

Other:
- [Fixing lambda](https://stupidpythonideas.blogspot.com/2014/02/fixing-lambda.html) - A blog post about alternative lambda syntaxes.
- [Mini-lambda](https://smarie.github.io/python-mini-lambda/#see-also) - Packages to "fix" lambda.
- [Meta](https://srossross.github.io/Meta/html/) - A few utils to work on AST's.
- [latexify](https://github.com/google/latexify_py) - Converts python to LaTeX.

Useful references:
- [python macros use cases](https://stackoverflow.com/questions/764412/python-macros-use-cases) - Stack-overflow discussion.
- [Green tree snakes](https://greentreesnakes.readthedocs.io/en/latest/) - Documention about AST.
