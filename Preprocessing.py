# Team 5
# José Ángel García Gómez - A01745865
# David Damian Galan - A01752785
# Luis Humberto Romero Pérez - A01752789
# File or class that contains all preprocessing functions for the tool
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
 

class Preprocessing:
    
    def __init__(self):
        self.current_text = ''
        self.processed_text = ''
        self.sentences = []
        self.word_list = []
        self.n_grams = []
    
    def set_text(self, text):
        self.current_text = text

    # Text cleaning
    def to_lower_without_punctuation(self):
        final_headline = ""
        for c in self.current_text:
            if c >= 'a' and c <= 'z' or c == ' ' or c >= 'A' and c <= 'Z' or c == '.':
                final_headline += c
        return final_headline.lower()
    
    def sentence_separation(self):
        self.sentences = self.current_text.split('.')
    
    def stopword_removal(self):
        stop_words = set(stopwords.words('english'))
        word_tokens = word_tokenize(self.current_text)
        filtered_sentence = [w for w in word_tokens if not w in stop_words]
        print(filtered_sentence)
        return filtered_sentence

    # Word separation (stopwords, lemmatization)

    # N-grams