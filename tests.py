import unittest

class MyTestCase(unittest.TestCase):
    def test_something(self):
        answer = 42
        self.assertEqual(answer, 42)

unittest.main()
