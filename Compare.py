# Team 5
# José Ángel García Gómez - A01745865
# David Damian Galan - A01752785
# Luis Humberto Romero Pérez - A01752789
# File or class that contains all functions to calculate the similitude between two texts
from Preprocessing import Preprocessing
from pprint import pprint
class Compare:

    def __init__(self, dictionary):
        self.is_plagiarism = False
        self.textToCompare = ''
        self.dictionary = dictionary
        self.text_n_grams = []
        self.preproccess_module = Preprocessing()
    
    def read_text(self,text_path):
        file = open(text_path, "r")
        content = file.read()
        self.textToCompare = content
        file.close()
        return self.textToCompare

    def preprocess_data(self):
        self.preproccess_module.set_text(self.textToCompare)
        self.preproccess_module.preprocess_data()
        self.text_n_grams = self.preproccess_module.n_grams
        return self.text_n_grams

    def get_similarity_score(self, sentence1_ngrams, sentence2_ngrams):
        set_sentence1 = set(sentence1_ngrams)
        set_sentence2 = set(sentence2_ngrams)
        ngrams_both = set_sentence1.intersection(set_sentence2)
        ngrams_list = set_sentence1.union(set_sentence2)
        score = len(ngrams_both) / len(ngrams_list)
        return round(score, 2)

    def get_similarity_matrix(self, paragraph1, paragraph2):
        similarities_matrix = []
        for sentence2 in paragraph2:
            sentence_similarity = []
            for sentence1 in paragraph1:
                score = self.get_similarity_score(sentence1, sentence2)
                sentence_similarity.append(score)
            similarities_matrix.append(sentence_similarity)
        return similarities_matrix

    def compare(self, text_path):
        self.read_text(text_path)
        self.preprocess_data()
        for key in self.dictionary:
            similarities_matrix = self.get_similarity_matrix(self.dictionary[key], self.text_n_grams)
            mean_score = 0
            for sentence in similarities_matrix:
                sentence_score = max(sentence)
                mean_score += sentence_score
            mean_score = mean_score / len(similarities_matrix)
            if mean_score >= 0.6:
                self.is_plagiarism = True
                return (self.is_plagiarism, key, mean_score)
        return (self.is_plagiarism, None, None)