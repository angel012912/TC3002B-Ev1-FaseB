"""
Team 5
José Ángel García Gómez - A01745865
David Damian Galan - A01752785
Luis Humberto Romero Pérez - A01752789
Main file of the tool, contains the correspondent process to ask the tool to validate the similarity of a given text
"""
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
        result = self.dictionary.folder_text_reading(os.path.join(self.dir_path, 'Data/anotherTestTextFolder'))
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

    # Test preprocess module
    def test_10(self):
        self.dictionary.text_reading(os.path.join(self.dir_path, 'Data/text.txt'))
        self.assertEqual('this is a test text file information', self.dictionary.preprocess_module.current_text)
    
    # Test preprocess module set text
    def test_11(self):
        self.dictionary.preprocess_module.set_text('Some text to test the set text function')
        self.assertEqual('Some text to test the set text function', self.dictionary.preprocess_module.current_text)
    
    # Test preprocess module preprocess data - to lower without punctuation
    def test_12(self):
        self.dictionary.preprocess_module.set_text('!Some ?text _to =test {the s/et text function')
        self.dictionary.preprocess_module.to_lower_without_punctuation()
        self.assertEqual('some text to test the set text function', self.dictionary.preprocess_module.current_text)

    # Test preprocess module preprocess data - sentence separation
    def test_13(self):
        self.dictionary.preprocess_module.set_text('This is a test. This is another test.')
        self.dictionary.preprocess_module.sentence_separation()
        self.assertEqual(['This is a test', ' This is another test'], self.dictionary.preprocess_module.sentences)

    # Test preprocess module preprocess data - stopword removal
    def test_14(self):
        self.dictionary.preprocess_module.set_text('This is a test. This is another test.')
        self.dictionary.preprocess_module.sentence_separation()
        self.dictionary.preprocess_module.stopword_removal()
        self.assertEqual([['This', 'test'], ['This', 'another', 'test']], self.dictionary.preprocess_module.word_list)

    # Test preprocess module preprocess data - lemmatize words
    def test_15(self):
        self.dictionary.preprocess_module.set_text('This tests have been used a lot')
        self.dictionary.preprocess_module.sentence_separation()
        self.dictionary.preprocess_module.stopword_removal()
        self.dictionary.preprocess_module.lemmatize_words()
        self.assertEqual([['This', 'test', 'used', 'lot']], self.dictionary.preprocess_module.word_list)

    # Test preprocess module preprocess data - create n grams
    def test_16(self):
        self.dictionary.preprocess_module.set_text('This tests have been used a lot')
        self.dictionary.preprocess_module.sentence_separation()
        self.dictionary.preprocess_module.stopword_removal()
        self.dictionary.preprocess_module.lemmatize_words()
        self.dictionary.preprocess_module.create_n_grams(range(2,4))
        self.assertEqual([[[('This', 'test'), ('test', 'used'), ('used', 'lot')]], [[('This', 'test', 'used'), ('test', 'used', 'lot')]]], self.dictionary.preprocess_module.n_grams)
    
    # Test preprocess module preprocess data - preprocess data
    def test_17(self):
        self.dictionary.preprocess_module.set_text('This tests have been used a lot that 5 words to test')
        self.dictionary.preprocess_module.preprocess_data()
        self.assertEqual([[[('test', 'used'), ('used', 'lot'), ('lot', 'word'), ('word', 'test')]], [[('test', 'used', 'lot'), ('used', 'lot', 'word'), ('lot', 'word', 'test')]], [[('test', 'used', 'lot', 'word'), ('used', 'lot', 'word', 'test')]], [[('test', 'used', 'lot', 'word', 'test')]]], self.dictionary.preprocess_module.n_grams)

    # Test update dictionary function
    def test_18(self):
        self.maxDiff = None
        self.dictionary.text_reading('Data/text.txt', self.dir_path)
        self.dictionary.update_dictionary('Data/text.txt')
        self.assertEqual({'Data/text.txt': [[[('test', 'text'), ('text', 'file'), ('file', 'information')]], [[('test', 'text', 'file'), ('text', 'file', 'information')]], [[('test', 'text', 'file', 'information')]], []]}, self.dictionary.dictionary)

