from unittest import TestCase
from Compare import Compare

class TestCompare(TestCase):

    # Test correct initialization
        # Test textToCompare
        # Test N-grams
        # Test dictionary
        # Test no-empty dictionary
    
    # Test read_text function
        # Test text reading
        # Test textToCompare

    # Test preprocess_data function
        # Test preprocess_data
        # Test text_n_grams

    # Test get_similarity_score function
        # Test similarity score
            # Test sentences with no similarity
            # Test sentences with total similarity
            # Test sentences with partial similarity
        # Test error handling
            # Test empty sentences
            # Test empty n-grams
            # Test differents n-grams orders
    
    # Test get_similarity_matrix function
        # Test similarity matrix 
            # Test paragraphs with no similarity
            # Test paragraphs with total similarity
            # Test paragraphs with partial similarity
        # Test error handling
            # Test empty paragraphs
            # Test empty n-grams
            # Test differents n-grams orders
    
    # Test compare function
        # Test comparison
            # Test total plagiarism
            # Test plagiarism with different texts
            # Test minimal plagiarism
            # Test partial plagiarism
            # Test partial plagiarism with different texts
            # Test minimal plagiarism with different texts
            # Test no plagiarism
        # Test error handling
            # Test empty text


    # def setUp(self):
    #     self.compare = Compare()

    def test_0(self):
        self.assertEqual(
            0,
            0)