from unittest import TestCase

from uneval import expr, evaluate, scoped


class TestScoped(TestCase):
    def test_nameerror(self):
        """Test that expression ignores scope."""
        x = 3
        assert x > 0  # Suppress unused warnings

        with self.assertRaises(NameError):
            evaluate(expr("x + 5"))

    def test_kwarg(self):
        """Test that scope can be augmented."""
        result = evaluate(scoped("x + 5"), x = 3)
        expected = 8
        self.assertEqual(expected, result)

    def test_scoped(self):
        """Test that scope does capture scope."""
        x = 3
        assert x > 0  # Suppress unused warnings
        result = evaluate(scoped("x + 5"))
        expected = 8
        self.assertEqual(expected, result)
