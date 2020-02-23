import unittest
import os

from main import cleanTextFiles

class TestMainMethods(unittest.TestCase):

    def setUp(self):
        self.data_folder = os.path.join(os.path.expanduser("~"),
                                        "Documents/repos/keywordAnalysis/data")
                                
        self.stop_words = {"one", "two"}

    # test with no file names
    def test_emptyInputs(self):

        emptyFileList = []

        result = len(cleanTextFiles(self.data_folder, emptyFileList, 
                                    self.stop_words))

        self.assertEqual(result, 0)

    # test return with 1 file
    def test_oneFile(self):

        fileList = ["Apple_Event_2017_09.txt"]

        result = len(cleanTextFiles(self.data_folder, fileList, 
                                    self.stop_words))

        self.assertEqual(result, 1)