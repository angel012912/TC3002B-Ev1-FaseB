"""
Team 5
José Ángel García Gómez - A01745865
David Damian Galan - A01752785
Luis Humberto Romero Pérez - A01752789
Main file of the tool, contains the correspondent process to ask the tool to validate the similarity of a given text
"""
from unittest import TestCase
from Compare import Compare
from Dictionary import Dictionary
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

class TestCompare(TestCase):

    def setUp(self):
        self.dir_path = dir_path
        self.dictionary = Dictionary()
        self.dictionary.text_reading('Data/text.txt', self.dir_path)
        self.compare = Compare(self.dictionary.dictionary)

    # Test correct initialization - Test textToCompare
    def test_0(self):
        self.assertEqual(
            '',
            self.compare.textToCompare)
    
    # Test correct initialization - Test text_n_grams
    def test_1(self):
        self.assertEqual(
            [],
            self.compare.text_n_grams)
    
    # Test correct initialization - Test dictionary
    def test_2(self):
        self.assertEqual(
            {'Data/text.txt': [[[('test', 'text'), ('text', 'file'), ('file', 'information')]], [[('test', 'text', 'file'), ('text', 'file', 'information')]], [[('test', 'text', 'file', 'information')]], []]},
            self.compare.dictionary)
    
    # Test dictionary - Test no-empty dictionary
    def test_3(self):
        self.assertNotEqual(
            {},
            self.compare.dictionary)

    # Test read_text function - Test text reading
    def test_4(self):
        self.assertEqual(
            'This is a test text file information',
            self.compare.read_text(os.path.join(self.dir_path, 'Data/text.txt')))
    
    # Test read_text function - Test txt file with no text
    def test_5(self):
        with self.assertRaises(Exception):
            self.compare.read_text(os.path.join(self.dir_path, 'Data/noText.txt'))
        
    # Test read_text function - Test wrong path
    def test_6(self):
        with self.assertRaises(FileNotFoundError):
            self.compare.read_text(os.path.join(self.dir_path, 'Data/wrongPath.txt'))
        
    # Test read_text function - Test a path with no .txt extension
    def test_7(self):
        with self.assertRaises(Exception):
            self.compare.read_text(os.path.join(self.dir_path, 'Data/noTextsFolder/ex1.pdf'))
    
    # Test read_text function - Test textToCompare
    def test_8(self):
        self.compare.read_text(os.path.join(self.dir_path, 'Data/text.txt'))
        self.assertEqual(
            'This is a test text file information',
            self.compare.textToCompare)

    # Test preprocess_data function - Test text_n_grams
    def test_9(self):
        self.compare.read_text(os.path.join(self.dir_path, 'Data/text.txt'))
        self.compare.preprocess_data()
        self.assertEqual(
            [[[('test', 'text'), ('text', 'file'), ('file', 'information')]], [[('test', 'text', 'file'), ('text', 'file', 'information')]], [[('test', 'text', 'file', 'information')]], []],
            self.compare.text_n_grams)

    # Test get_similarity_score function - Test sentences with no similarity
    def test_10(self):
        self.assertEqual(
            0,
            self.compare.get_similarity_score([('test', 'text'), ('no', 'similarity')], [('file', 'information'), ('nothing', 'similar')]))
    
    # Test get_similarity_score function - Test sentences with total similarity
    def test_11(self):
        self.assertEqual(
            1,
            self.compare.get_similarity_score([('test', 'text'), ('ultra', 'equal')], [('test', 'text'), ('ultra', 'equal')]))
    
    # Test get_similarity_score function - Test sentences with partial similarity
    def test_12(self):
        self.assertEqual(
            0.5,
            self.compare.get_similarity_score([('test', 'text'), ('partial', 'similarity'), ('one', 'same')], [('test', 'text'), ('total', 'similarity'), ('one', 'same')]))
    
    # Test get_similarity_score function - Test empty sentences
    def test_13(self):
        self.assertEqual(
            0,
            self.compare.get_similarity_score([], [('file', 'information'), ('nothing', 'similar')]))
    
    # Test get_similarity_score function - Test empty n-grams
    def test_14(self):
        self.assertEqual(
            0,
            self.compare.get_similarity_score([('test', 'text'), ('no', 'similarity')], [(), ()]))
    
    # Test get_similarity_score function - Test differents n-grams orders
    def test_15(self):
        self.assertEqual(
            0,
            self.compare.get_similarity_score([('test', 'text', 'to'), ('partial', 'similarity', 'compare'), ('one', 'same', 'range')], [('one', 'same'), ('test', 'text'), ('total', 'similarity')]))
    
    # Test get_similarity_matrix function - Test paragraphs with no similarity
    def test_16(self):
        self.assertEqual(
            [[0, 0], [0, 0]],
            self.compare.get_similarity_matrix([('test', 'text'), ('no', 'similarity')], [('file', 'information'), ('nothing', 'similar')]))
    
    # Test get_similarity_matrix function - Test paragraphs with total similarity
    def test_17(self):
        self.assertEqual(
            [[1.0, 0.0], [0.0, 1.0]],
            self.compare.get_similarity_matrix([('test', 'text'), ('ultra', 'equal')], [('test', 'text'), ('ultra', 'equal')]))
    
    # Test get_similarity_matrix function - Test paragraphs with partial similarity
    def test_18(self):
        self.assertEqual(
            [[1.0, 0.0, 0.0], [0.0, 0.33, 0.0], [0.0, 0.0, 1.0]],
            self.compare.get_similarity_matrix([('test', 'text'), ('partial', 'similarity'), ('one', 'same')], [('test', 'text'), ('total', 'similarity'), ('one', 'same')]))
    
    # Test get_similarity_matrix function - Test empty paragraphs
    def test_19(self):
        self.assertEqual(
            [[], []],
            self.compare.get_similarity_matrix([], [('file', 'information'), ('nothing', 'similar')]))
    
    # Test get_similarity_matrix function - Test empty n-grams
    def test_20(self):
        self.assertEqual(
            [[0, 0], [0, 0]],
            self.compare.get_similarity_matrix([('test', 'text'), ('no', 'similarity')], [(), ()]))
    
    # Test compare function - Test total plagiarism
    def test_21(self):
        self.compare.read_text(os.path.join(self.dir_path, 'Data/text.txt'))
        self.compare.preprocess_data()
        self.assertEqual(
            (True, '1.00', [('Data/text.txt', 1.00)]),
            self.compare.compare(os.path.join(self.dir_path, 'Data/text.txt')))

    # Test compare function - Test plagiarism with different texts
    def test_22(self):
        newDictionary = Dictionary()
        newDictionary.folder_text_reading(os.path.join(self.dir_path, 'Data/textsFolder'))
        compare = Compare(newDictionary.dictionary)
        result = compare.compare(os.path.join(self.dir_path, 'Data/txtSomeTexts.txt'))
        expected_cases = [(True, '1.00', [('txtPlag2.txt', 0.50), ('txtPlag1.txt', 0.50)]), (True, '1.00', [('txtPlag1.txt', 0.50), ('txtPlag2.txt', 0.50)])]
        self.assertIn(result, expected_cases)
    
    # Test compare function - Test minimal plagiarism
    def test_23(self):
        newDictionary = Dictionary()
        newDictionary.folder_text_reading(os.path.join(self.dir_path, 'Data/textsFolder'))
        compare = Compare(newDictionary.dictionary)
        self.assertEqual(
            '0.26',
            compare.compare(os.path.join(self.dir_path, 'Data/txtMinimal.txt'))[1])

    # Test compare function - Test empty text
    def test_24(self):
        with self.assertRaises(Exception):
            self.compare.compare(os.path.join(self.dir_path, 'Data/noText.txt'))

