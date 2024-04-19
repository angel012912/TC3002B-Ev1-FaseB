from unittest import TestCase
from Preprocessing import Preprocessing

class TestPreprocessing(TestCase):

    # Test correct initialization
        # Test current_text
        # Test processed_text
        # Test sentences
        # Test word_list
        # Test n_grams
    
    # Test set_text function
        # Test current_text
    
    # Test to_lower_without_punctuation function
        # Test punctuation removal
        # Test lowercase conversion
        # Test words kept
    
    # Test stopword_removal function
        # Test stopwords removal
        # Test word_list
        # Test non-stopwords kept
    
    # Test sentence_separation function
        # Test sentence separation
        # Test sentences
        # Test empty sentence removal
    
    # Test lemmatize_words function
        # Test lemmatization
        # Test word_list
        # Test lemmatization of words
    
    # Test create_n_grams function
        # Test n_grams creation
        # Test n_grams
        # Test n_grams range
        # Test n_grams creation for each sentence
        # Test n_grams size
    
    # Test preprocess_data function
        # Test n_grams creation from raw text
        # Test n_grams withouth punctuation and stopwords
        # Test n_grams words lemmatization
        # Test n_grams creation for each sentence
        # Test n_grams size
        # Test n_grams range

    # def setUp(self):
    #     self.preprocessing = Preprocessing()

    def test_0(self):
        self.assertEqual(
            0,
            0)