from unittest import TestCase
from Main import Main
from unittest import mock
import Compare
import Dictionary
import os

dir_name = os.path.dirname(os.path.realpath(__file__))

class TestMain(TestCase):

    # Test correct initialization
        # Test dictionary
            # Test the folder text reading
            # Test the folder dictionary
            # Test the text text reading
            # Test the text dictionary
        # Test compare_module
            # Test the compare dictionary

    # Test compare
        # Test the compare function
        # Test the compare with empty text
        # Test the compare with a wrong path
        # Test the compare with a correct path
        # Test the compare with a path with no .txt extension
        # Test the compare with a identical text to a text in the dictionary
        # Test the compare with a text that is not in the dictionary
        # Test the compare with a text that is in the dictionary but is not identical
        # Test the compare with a text with minimal similarity
        # Test the compare with a text with minimal similarity with some texts
        # Test the compare with a text with minimal similarity with some texts that the sum of the similarities is greater equal than the minimal
        # Test the compare folder function
        # Test the compare folder function with a folder with no .txt files
        # Test the compare folder function with wrong path
        # Test the compare folder function with texts that has no plagiarism
        # Test the compare folder function with texts that has one plagiarism
        # Test the compare folder function with texts that has multiple plagiarism
        # Test the compare folder function with texts that has multiple plagiarism with some texts that the sum of the similarities is greater equal than the minimal
        # Test the compare folder function with texts that has multiple plagiarism with some texts that the sum of the similarities is the 100% of the text


    def setUp(self):
        self.main = Main(os.path.join(dir_name, "../TestData"))
         # Path to the test data folder

    def test_0(self):
        self.assertEqual(
            0,
            0)
    
    """
    Function to mock the behaviour of Compare.compare
    Returns a tuple with
    (
        File is plagiarism (boolean),
        Percentage of coincidences (float),
        List of tuples of files with coincidences ((filename, percentage))
    )
    """
    def compare_mock(self, text_path):
        return (True, 0.67, [(text_path, 0.67)])

    # Test the main.compare function calls the Compare.compare function
    @mock.patch('Compare.Compare.compare', new=compare_mock)
    def test_xx(self):
        self.assertEqual(self.main.compare("my_file.txt"),
                         (True, 0.67, [('my_file.txt', 0.67)]))
        