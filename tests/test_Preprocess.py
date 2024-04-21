"""
Team 5
José Ángel García Gómez - A01745865
David Damian Galan - A01752785
Luis Humberto Romero Pérez - A01752789
Main file of the tool, contains the correspondent process to ask the tool to validate the similarity of a given text
"""
from unittest import TestCase
from Preprocessing import Preprocessing

class TestPreprocessing(TestCase):

    def setUp(self):
        self.preprocessing = Preprocessing()
    
    # Test correct initialization  - Test current_text
    def test_0(self):
        self.assertEqual(
            '',
            self.preprocessing.current_text)
    
    # Test correct initialization  - Test processed_text
    def test_1(self):
        self.assertEqual(
            '',
            self.preprocessing.processed_text)
        
    # Test correct initialization  - Test sentences
    def test_2(self):
        self.assertEqual(
            [],
            self.preprocessing.sentences)
        
    # Test correct initialization  - Test word_list
    def test_3(self):
        self.assertEqual(
            [],
            self.preprocessing.word_list)
        
    # Test correct initialization  - Test n_grams
    def test_4(self):
        self.assertEqual(
            [],
            self.preprocessing.n_grams)
    
    # Test set_text function - Test current_text
    def test_5(self):
        self.assertEqual(
            'This is a test',
            self.preprocessing.set_text('This is a test'))

    # Test to_lower_without_punctuation function - Test lowercase conversion
    def test_6(self):
        self.preprocessing.set_text('This is a test')
        self.assertEqual(
            'this is a test',
            self.preprocessing.to_lower_without_punctuation())
    
    # Test to_lower_without_punctuation function - Test punctuation removal
    def test_7(self):
        self.preprocessing.set_text('!This???? ???is !!a" "test".')
        self.assertEqual(
            'this is a test.',
            self.preprocessing.to_lower_without_punctuation())
     
    # Test to_lower_without_punctuation function - Test words kept
    def test_8(self):
        self.preprocessing.set_text('This is a test w!i"th p_u_n_c_t_u_a_t_i_o_n_')
        self.assertEqual(
            'this is a test with punctuation',
            self.preprocessing.to_lower_without_punctuation())
    
    # Test stopword_removal function - Test stopwords removal
    def test_9(self):
        self.preprocessing.set_text('This is a test with stopwords.')
        self.preprocessing.to_lower_without_punctuation()
        self.preprocessing.sentence_separation()
        self.assertEqual(
            [['test', 'stopwords']],
            self.preprocessing.stopword_removal())
    
    # Test stopword_removal function - Test word_list    
    def test_10(self):
        self.preprocessing.set_text('This is a test with stopwords.')
        self.preprocessing.to_lower_without_punctuation()
        self.preprocessing.sentence_separation()
        self.preprocessing.stopword_removal()
        self.assertEqual(
            2,
            len(self.preprocessing.word_list[0]))

    # Test stopword_removal function - Test non-stopwords kept
    def test_11(self):
        self.preprocessing.set_text('This is a test with stopwords, but not all of them will stay, only the stopwords.')
        self.preprocessing.to_lower_without_punctuation()
        self.preprocessing.sentence_separation()
        self.preprocessing.stopword_removal()
        self.assertEqual(
            [['test', 'stopwords', 'stay', 'stopwords']],
            self.preprocessing.word_list)
    
    # Test sentence_separation function - Test sentence separation
    def test_12(self):
        self.preprocessing.set_text('This is a test. This is another test.')
        self.preprocessing.to_lower_without_punctuation()
        self.assertEqual(
            ['this is a test', ' this is another test'],
            self.preprocessing.sentence_separation())
    
    # Test sentence_separation function - Test sentences
    def test_13(self):
        self.preprocessing.set_text('This is a test. This is another test.')
        self.preprocessing.to_lower_without_punctuation()
        self.preprocessing.sentence_separation()
        self.assertEqual(
            2,
            len(self.preprocessing.sentences))
        
    # Test sentence_separation function - Test empty sentence removal
    def test_14(self):
        self.preprocessing.set_text('This is a test. This is another test. .')
        self.preprocessing.to_lower_without_punctuation()
        self.preprocessing.sentence_separation()
        self.assertEqual(
            2,
            len(self.preprocessing.sentences))
    
    # Test lemmatize_words function - Test lemmatization
    def test_15(self):
        self.preprocessing.set_text('This is a tests with words lemmatized .')
        self.preprocessing.to_lower_without_punctuation()
        self.preprocessing.sentence_separation()
        self.preprocessing.stopword_removal()
        self.assertEqual(
            [['test', 'word', 'lemmatized']],
            self.preprocessing.lemmatize_words())
    
    # Test lemmatize_words function - Test word_list
    def test_16(self):
        self.preprocessing.set_text('This is a tests with lemmatizations, but not all of them will be lemmatized.')
        self.preprocessing.to_lower_without_punctuation()
        self.preprocessing.sentence_separation()
        self.preprocessing.stopword_removal()
        self.preprocessing.lemmatize_words()
        self.assertEqual(
            3,
            len(self.preprocessing.word_list[0]))
    
    # Test create_n_grams function - Test n_grams creation
    def test_17(self):
        self.preprocessing.set_text('This is a test with n-grams.')
        self.preprocessing.to_lower_without_punctuation()
        self.preprocessing.sentence_separation()
        self.preprocessing.stopword_removal()
        self.preprocessing.lemmatize_words()
        self.assertIsInstance(
            self.preprocessing.create_n_grams([2])[0][0][0],
            tuple)

    # Test create_n_grams function - Test n_grams
    def test_18(self):
        self.preprocessing.set_text('This is a test with n-grams.')
        self.preprocessing.to_lower_without_punctuation()
        self.preprocessing.sentence_separation()
        self.preprocessing.stopword_removal()
        self.preprocessing.lemmatize_words()
        self.preprocessing.create_n_grams([2])
        self.assertEqual(
            ('test', 'ngrams'),
            self.preprocessing.n_grams[0][0][0])
    
    # Test create_n_grams function - Test n_grams range
    def test_19(self):
        self.preprocessing.set_text('This is a test with n-grams, that has a lot of words so the n-grams range will be asserted for each one, and the n-grams will be created for each sentence, and this text has to be long enough to create n-grams of different sizes.')
        self.preprocessing.to_lower_without_punctuation()
        self.preprocessing.sentence_separation()
        self.preprocessing.stopword_removal()
        self.preprocessing.lemmatize_words()
        self.preprocessing.create_n_grams(range(2, 10))
        self.assertEqual(
            8,
            len(self.preprocessing.n_grams))

    # Test create_n_grams function - Test n_grams creation for each sentence
    def test_20(self):
        self.preprocessing.set_text('This is a test with n-grams. This is another test with n-grams.')
        self.preprocessing.to_lower_without_punctuation()
        self.preprocessing.sentence_separation()
        self.preprocessing.stopword_removal()
        self.preprocessing.lemmatize_words()
        self.preprocessing.create_n_grams([2])
        self.assertEqual(
            2,
            len(self.preprocessing.n_grams[0]))
    
    # Test create_n_grams function - Test n_grams size
    def test_21(self):
        self.preprocessing.set_text('This is a test with n-grams that can generate n-grams of size 5.')
        self.preprocessing.to_lower_without_punctuation()
        self.preprocessing.sentence_separation()
        self.preprocessing.stopword_removal()
        self.preprocessing.lemmatize_words()
        self.preprocessing.create_n_grams([5])
        self.assertEqual(
            5,
            len(self.preprocessing.n_grams[0][0][0]))
    
    # Test preprocess_data function - Test n_grams creation with text with punctuation and capitalized words
    def test_22(self):
        self.preprocessing.set_text('This is a raw text with punctuation, and capitalized words.')
        self.preprocessing.sentence_separation()
        self.preprocessing.stopword_removal()
        self.preprocessing.lemmatize_words()
        self.preprocessing.create_n_grams([2])
        self.assertEqual(
            [('This', 'raw'), ('raw', 'text'), ('text', 'punctuation'), ('punctuation', ','), (',', 'capitalized'), ('capitalized', 'word')],
            self.preprocessing.n_grams[0][0])

    # Test preprocess_data function - Test n_grams creation for each sentence
    def test_23(self):
        self.preprocessing.set_text('This is a test with n-grams. This is another test with n-grams.')
        self.preprocessing.preprocess_data()
        self.assertEqual(
            2,
            len(self.preprocessing.n_grams[0]))
    
    # Test preprocess_data function - Test n_grams size of the first n-gram iteration
    def test_24(self):
        self.preprocessing.set_text('This is a test with n-grams that can generate n-grams of size 2.')
        self.preprocessing.preprocess_data()
        self.assertEqual(
            2,
            len(self.preprocessing.n_grams[0][0][0]))
    
    # Test preprocess_data function - Test n_grams size of the second n-gram iteration
    def test_25(self):
        self.preprocessing.set_text('This is a test with n-grams that can generate n-grams of size 3.')
        self.preprocessing.preprocess_data()
        self.assertEqual(
            3,
            len(self.preprocessing.n_grams[1][0][0]))

    # Test preprocess_data function - Test n_grams size of the third n-gram iteration
    def test_26(self):
        self.preprocessing.set_text('This is a test with n-grams that can generate n-grams of size 4.')
        self.preprocessing.preprocess_data()
        self.assertEqual(
            4,
            len(self.preprocessing.n_grams[2][0][0]))

    # Test preprocess_data function - Test n_grams size of the fourth n-gram iteration
    def test_27(self):
        self.preprocessing.set_text('This is a test with n-grams that can generate n-grams of size 5.')
        self.preprocessing.preprocess_data()
        self.assertEqual(
            5,
            len(self.preprocessing.n_grams[3][0][0]))
