"""
Team 5
José Ángel García Gómez - A01745865
David Damian Galan - A01752785
Luis Humberto Romero Pérez - A01752789
File or class that contains the correspondent process to create or update de n-grams dictionary for the tool
"""

# Libraries
import os
from Preprocessing import Preprocessing

class Dictionary:

    """
    Constructor for the class Dictionary, it initializes the dictionary of the tool
    the current text that is being processed an instance of the Preprocessing class.
    """
    def __init__(self):
        self.dictionary = {}
        self.current_text = ''
        self.preprocess_module = Preprocessing()

    """
    Document Reading Function, reads a text file according to the file and folder
    path given as strings, it preprocesses the data and updates the dictionary.
    """
    def text_reading(self, text_path, folder_path=''):
        file = open(folder_path+"/"+text_path, "r", encoding="utf-8") if folder_path else open(text_path, "r", encoding="utf-8")
        content = file.read()
        if content == '':
            raise Exception("The file is empty")
        self.current_text = content
        self.preprocess_data()
        self.update_dictionary(text_path)
        file.close()
        return self.current_text
    
    """
    Folder Text Reading Function, reads all the text files in the folder of the
    path given as a string.    
    """
    def folder_text_reading(self, folder_path):
        if not os.listdir(folder_path):
            raise Exception("The folder is empty")
        content_readed_list = []
        for file_path in os.listdir(folder_path):
            if file_path.endswith(".txt"):
                try:
                    content_readed = self.text_reading(file_path, folder_path)
                    content_readed_list.append(content_readed)
                except Exception as e:
                    print(e)
        if not content_readed_list:
            raise Exception("The folder has no text files")
        return content_readed_list
    
    """
    Preprocess Data Function, preprocesses the data of the saved text using the
    functions in the Preprocessing class.
    """
    def preprocess_data(self):
        self.preprocess_module.set_text(self.current_text)
        self.preprocess_module.preprocess_data()
    
    """
    Update Dictionary Function, updates the dictionary with the n-grams of the
    text that was just processed.
    """
    def update_dictionary(self, text_path):
        self.dictionary[text_path] = self.preprocess_module.n_grams
        return self.dictionary
