import ast
from unittest import TestCase

from uneval import var, evaluate, expr


class TestUneval(TestCase):
    def setUp(self):
        self.squares = [
            "x * x",
            expr("x * x"),
            var.x * var.x,
            ast.parse("x * x", mode="eval")
        ]

    def test_evaluate(self):
        for square in self.squares:
            with self.subTest(msg=square):
                res = evaluate(square, x=3)
                self.assertEqual(9, res)
