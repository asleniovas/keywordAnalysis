import unittest

from modules.textCounter import TextCounter

class TestTextCounterMethods(unittest.TestCase):

    def setUp(self):
        self.counter = TextCounter()

    # test that return is a subclass of dict
    def test_returnType(self):

        emptyList = []

        result = type(self.counter.countElements(emptyList))

        self.assertTrue(issubclass(result, dict))

    #test return lenght based on example
    def test_returnLength(self):

        exampleList = ["one", "two", "one"]

        result = len(self.counter.countElements(exampleList))

        self.assertEqual(result, 2)