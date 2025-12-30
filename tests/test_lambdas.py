from unittest import TestCase

from uneval import expr, evaluate, scoped, F, var


class TestLambdas(TestCase):
    def test_nameerror(self):
        """Test that expression ignores scope."""
        y = 9
        assert y > 0  # Suppress unused warnings
        my_fun = F.x(abs(var.x - var.y))

        with self.assertRaises(NameError):
            my_fun(3)

    def test_kwarg(self):
        """Test that scope can be augmented."""
        my_fun = F.x(var.abs(var.x - var.y), y = 9)
        result = my_fun(3)
        expected = 6
        self.assertEqual(expected, result)

    def test_scoped(self):
        """Test that scope does capture scope."""
        y = 9
        assert y > 0  # Suppress unused warnings
        my_fun = F.x(scoped(abs(var.x - var.y)))
        result = my_fun(3)
        expected = 6
        self.assertEqual(expected, result)
