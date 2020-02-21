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

if __name__ == '__main__':
    unittest.main()    