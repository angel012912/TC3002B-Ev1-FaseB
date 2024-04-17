# Team 5
# José Ángel García Gómez - A01745865
# David Damian Galan - A01752785
# Luis Humberto Romero Pérez - A01752789
# File or class that contains the correspondent process to create or update de n-grams dictionary for the tool

# Libraries
import os
from Preprocessing import Preprocessing
from pprint import pprint

class Dictionary:

    def __init__(self):
        self.dictionary = ''
        self.current_text = ''
        self.preprocess_module = Preprocessing()

    # Document Reading Function
    def text_reading(self, text_path):
        file = open(text_path, "r")
        content = file.read()
        self.current_text = content
        self.preprocess_data()
        file.close()
    
    def folder_text_reading(self, folder_path):
        for file in os.listdir(folder_path):
            if file.endswith(".txt"):
                self.text_reading(folder_path+"/"+file)

    def preprocess_data(self):
        self.preprocess_module.set_text(self.current_text)
        self.preprocess_module.to_lower_without_punctuation()
        self.preprocess_module.sentence_separation()
        self.preprocess_module.stopword_removal()
        self.preprocess_module.lemmatize_words()
        self.preprocess_module.create_n_grams(3)
        pprint(self.preprocess_module.n_grams)
    
    # Dictionary update

    
