"""
Team 5
José Ángel García Gómez - A01745865
David Damian Galan - A01752785
Luis Humberto Romero Pérez - A01752789
Main file of the tool, contains the correspondent process to ask the tool to validate the similarity of a given text(s)
"""

# Libraries
from Dictionary import Dictionary
from Compare import Compare
from pprint import pprint
import os

class Main:

    def __init__(self, path, model_path="", tokenizer_path=""):
        """
        Constructor for the class Main, it initializes the dictionary of the tool
        reading the text files in the given folder path.
        """
        self.dictionary = Dictionary()
        if (os.path.isdir(path)):
            self.dictionary.folder_text_reading(path)
        else:
            self.dictionary.text_reading(path)
        self.compare_module = Compare(self.dictionary.dictionary, model_path, tokenizer_path)
    
    def compare(self, path):
        """
        Compare Function, compares the text located in the text path with the
        texts in the dictionary, using the compare function in the Compare class.
        """
        if not os.path.exists(path):
            raise Exception("The path does not exist")
        elif (os.path.isdir(path)):
            return self.compare_folder(path)
        else:
            return self.compare_module.compare(path)
    
    def compare_folder(self, folder_path):
        """
        Compare Folder Function, compares all the text files in the folder path
        with the texts in the dictionary, using the compare function in the Compare class.
        """
        result = {}
        for file in os.listdir(folder_path):
            if file.endswith(".txt"):
                file_path = os.path.join(folder_path, file)
                file_comparation = self.compare_module.compare(file_path)
                result[file] = file_comparation
        return result

if __name__ == '__main__':
    reference_file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "Data")
    evaluate_file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "Final Testing")
    model_weights_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "Model", "model.h5")
    tokenizer_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "Model", "tokenizer.pickle")
    main = Main(reference_file_path, model_weights_path, tokenizer_path)
    result = main.compare(evaluate_file_path)
    pprint(result)