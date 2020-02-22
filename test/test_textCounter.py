import unittest

from modules.textCounter import TextCounter

class TestTextCounterMethods(unittest.TestCase):

    def setUp(self):
        self.counter = TextCounter()

    def test_returnType(self):

        emptyList = []

        result = type(self.counter.countElements(emptyList))

        self.assertTrue(issubclass(result, dict))