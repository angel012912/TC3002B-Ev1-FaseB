from unittest import TestCase
from Dictionary import Dictionary
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

class TestDictionary(TestCase):

    

    def setUp(self):
        self.dictionary = Dictionary()
        self.dir_path = dir_path

    # Test correct initialization
    def test_0(self):
        self.assertEqual(
            {},
            self.dictionary.dictionary)
    
    def test_1(self):
        self.assertEqual(
            '',
            self.dictionary.current_text)

    # Test text reading function - File with text
    def test_2(self):
        self.assertEqual(
            'This is a test text file information',
            self.dictionary.text_reading(os.path.join(self.dir_path, 'Data/text.txt')))
    
    # Test text reading function - File with no text
    def test_3(self):
        with self.assertRaises(Exception):
            self.dictionary.text_reading(os.path.join(self.dir_path, 'Data/noText.txt'))
    
    # Test text reading function - Wrong path
    def test_4(self):
        with self.assertRaises(FileNotFoundError):
            self.dictionary.text_reading(os.path.join(self.dir_path, 'Data/wrongPath.txt'))

    # Test folder text reading function - Empty folder
    def test_5(self):
        with self.assertRaises(Exception):
            self.dictionary.folder_text_reading(os.path.join(self.dir_path, 'Data/emptyFolder'))

    # Test folder text reading function - Folder with text files
    def test_6(self):
        result = self.dictionary.folder_text_reading(os.path.join(self.dir_path, 'Data/textsFolder'))
        expected_cases = [['This is a test one', 'This is a test two'], ['This is a test two', 'This is a test one']]
        for expected_case in expected_cases:
            self.assertCountEqual(result, expected_case)

    # Test folder text reading function - Folder with no text files
    def test_7(self):
        with self.assertRaises(Exception):
            self.dictionary.folder_text_reading(os.path.join(self.dir_path, 'Data/noTextsFolder'))    

    # Test folder text reading function - Folder with text files empty
    def test_8(self):
        with self.assertRaises(Exception):
            self.dictionary.folder_text_reading(os.path.join(self.dir_path, "/Data/emptyTextsFolder"))

    # Test folder text reading function - Wrong path
    def test_9(self):
        with self.assertRaises(Exception):
            self.dictionary.folder_text_reading(os.path.join(self.dir_path, "Data/unexistentFolder"))

    # Test preprocess data function
        # Test preprocess module
        # Test preprocess module set text
        # Test preprocess module preprocess data

    # Test update dictionary function
        # Test dictionary
        # Test preprocess module n grams