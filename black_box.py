import unittest


def suma(a, b):
    return a + b


class BlackBoxTest(unittest.TestCase):
    def test_add_positive(self):
        a = 1
        b = 2

        ans = suma(a, b)

        self.assertEqual(ans, 3)

    def test_add_negative(self):
        a = -10
        b = -5

        ans = suma(a, b)

        self.assertEqual(ans, -15)


if __name__ == "__main__":
    unittest.main()
