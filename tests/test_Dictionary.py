from unittest import TestCase
from Dictionary import Dictionary

class TestDictionary(TestCase):

    def setUp(self):
        self.dictionary = Dictionary()

    # Test correct initialization
    def test_0(self):
        self.assertEqual(
            {},
            self.dictionary.dictionary)
    
    def test_1(self):
        self.assertEqual(
            '',
            self.dictionary.current_text)
    
    # Test text reading function

    # Test text reading function - File with text
    def test_2(self):
        self.assertEqual(
            'This is a test text file information',
            self.dictionary.text_reading('/Users/angel/Documents/Tec/8vo Sem/TC3002B-Ev1-FaseB/tests/Data/text.txt'))
    
    # Test text reading function - File with no text
    def test_3(self):
        with self.assertRaises(Exception):
            self.dictionary.text_reading('/Users/angel/Documents/Tec/8vo Sem/TC3002B-Ev1-FaseB/tests/Data/noText.txt')
    
    # Test text reading function - Wrong path

    
    # Test folder text reading function

    # Test preprocess data function
        # Test preprocess module
        # Test preprocess module set text
        # Test preprocess module preprocess data

    # Test update dictionary function
        # Test dictionary
        # Test preprocess module n grams