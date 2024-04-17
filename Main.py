# Team 5
# José Ángel García Gómez - A01745865
# David Damian Galan - A01752785
# Luis Humberto Romero Pérez - A01752789
# Main file of the tool, contains the correspondent process to ask the tool to validate the similarity of a given text
from Dictionary import Dictionary
from pprint import pprint

if __name__ == '__main__':
    dictionary = Dictionary()
    #dictionary.text_reading("/Users/angel/Documents/Tec/8vo Sem/TC3002B-Ev1-FaseB/Data", "org-001.txt")
    dictionary.folder_text_reading("/Users/angel/Documents/Tec/8vo Sem/TC3002B-Ev1-FaseB/Data")
    pprint(dictionary.dictionary)