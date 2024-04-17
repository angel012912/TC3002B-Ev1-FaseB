# Team 5
# José Ángel García Gómez - A01745865
# David Damian Galan - A01752785
# Luis Humberto Romero Pérez - A01752789
# Main file of the tool, contains the correspondent process to ask the tool to validate the similarity of a given text
from Dictionary import Dictionary
from Compare import Compare
from pprint import pprint
import os

class Main:

    def __init__(self, path):
        self.dictionary = Dictionary()
        if (os.path.isdir(path)):
            self.dictionary.folder_text_reading(path)
        else:
            self.dictionary.text_reading(path)
        self.compare_module = Compare(self.dictionary.dictionary)
    
    def compare(self, text_path):
        return self.compare_module.compare(text_path)
    
    def compare_folder(self, folder_path):
        result = {}
        for file in os.listdir(folder_path):
            if file.endswith(".txt"):
                file_path = os.path.join(folder_path, file)
                file_comparation = self.compare_module.compare(file_path)
                result[file] = file_comparation
        return result

if __name__ == '__main__':
    main = Main("/Users/angel/Documents/Tec/8vo Sem/TC3002B-Ev1-FaseB/Data")
    result = main.compare_folder('/Users/angel/Documents/Tec/8vo Sem/TC3002B-Ev1-FaseB/TestData')
    pprint(result)