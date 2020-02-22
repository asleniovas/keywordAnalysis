import unittest
from modules.textCleaner import TextCleaner

class TestTextCleanerMethods(unittest.TestCase):

    def setUp(self):
        self.cleaner = TextCleaner()


    def test_emptyInputs(self):

        emptySet = {}
        emptyList = []

        emptyResult = len(self.cleaner.compareRemove(emptySet,emptyList))

        self.assertEqual(emptyResult, 0)

    def test_SingleInputs(self):

        emptySet = {}
        exampleList = ["one", "two", "three"]

        result = len(self.cleaner.compareRemove(emptySet,exampleList))

        self.assertEqual(result, 3)

    def test_returnType(self):

        exampleSet = {"one", "two", "three"}
        exampleList = ["one", "two", "three"]

        result = type(self.cleaner.compareRemove(exampleSet,exampleList))

        self.assertEqual(result, list)

    def test_returnResult(self):

        exampleSet = {"three", "four"}
        exampleList = ["one", "two"]

        result = self.cleaner.compareRemove(exampleSet,exampleList)

        self.assertEqual(result[0] == "one" and result[1] == "two", True)

if __name__ == '__main__':
    unittest.main()    