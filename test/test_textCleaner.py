import unittest

from modules.textCleaner import TextCleaner

class TestTextCleanerMethods(unittest.TestCase):

    def setUp(self):
        self.cleaner = TextCleaner()

    # test with empty set and list
    def test_emptyInputs(self):

        emptySet = {}
        emptyList = []

        emptyResult = len(self.cleaner.compareRemove(emptySet,emptyList))

        self.assertEqual(emptyResult, 0)

    # test with list only
    def test_SingleInputs(self):

        emptySet = {}
        exampleList = ["one", "two", "three"]

        result = len(self.cleaner.compareRemove(emptySet,exampleList))

        self.assertEqual(result, 3)

    # test that return is a list
    def test_returnType(self):

        exampleSet = {"one", "two", "three"}
        exampleList = ["one", "two", "three"]

        result = type(self.cleaner.compareRemove(exampleSet,exampleList))

        self.assertEqual(result, list)

    # test for correct return result
    # list should remain the same in the below case
    def test_returnResult(self):

        exampleSet = {"three", "four"}
        exampleList = ["one", "two"]

        result = self.cleaner.compareRemove(exampleSet,exampleList)

        self.assertEqual(result[0] == "one" and result[1] == "two", True)

if __name__ == '__main__':
    unittest.main()    