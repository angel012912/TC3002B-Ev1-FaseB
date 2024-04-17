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
    
    def compare(self, text_path):
        compare = Compare(self.dictionary.dictionary)
        return compare.compare(text_path)

if __name__ == '__main__':
    main = Main("/Users/angel/Documents/Tec/8vo Sem/TC3002B-Ev1-FaseB/Data")
    result = main.compare('text_to_compare.txt')
    pprint(result)