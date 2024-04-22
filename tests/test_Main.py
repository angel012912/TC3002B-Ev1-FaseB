"""
Team 5
José Ángel García Gómez - A01745865
David Damian Galan - A01752785
Luis Humberto Romero Pérez - A01752789
Main file of the tool, contains the correspondent process to ask the tool to validate the similarity of a given text
"""
from unittest import TestCase
from Main import Main
from unittest import mock
import os

dir_name = os.path.dirname(os.path.realpath(__file__))

class TestMain(TestCase):

    def setUp(self):
        self.main = Main(os.path.join(dir_name, "../TestData"))

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
    def test_01(self):
        self.assertEqual(self.main.compare("my_file.txt"),
                         (True, 0.67, [('my_file.txt', 0.67)]))
    
    def os_listdir_mock(self):
        return ["file_1.txt", "file_2.txt", "file_3.pdf"]
    
    # Test function goes through all txt files in the folder and returns an evaluation for each one
    @mock.patch('Compare.Compare.compare', new=compare_mock)
    @mock.patch('os.listdir', new=os_listdir_mock)
    def test_02(self):
        expected_result = [{"file_1.txt": (True, 0.67, [('some_folder\\file_1.txt', 0.67)]),
                           "file_2.txt": (True, 0.67, [('some_folder\\file_2.txt', 0.67)])},
                           {"file_1.txt": (True, 0.67, [('some_folder/file_1.txt', 0.67)]),
                           "file_2.txt": (True, 0.67, [('some_folder/file_2.txt', 0.67)])} 
                           ]
        self.assertIn(self.main.compare_folder("some_folder"), expected_result)