"""
Team 5
José Ángel García Gómez - A01745865
David Damian Galan - A01752785
Luis Humberto Romero Pérez - A01752789
File or class that contains all functions to calculate the similitude between two texts
"""

# Libraries
from Preprocessing import Preprocessing

class Compare:

    """
    Constructor for the class Compare, it initializes current text that is being analyzed
    an instance of the Preprocessing class, a given dictionary of texts to compare with
    and the list of n-grams of the text that is being analyzed.
    """
    def __init__(self, dictionary):
        self.textToCompare = ''
        self.dictionary = dictionary
        self.text_n_grams = []
        self.preproccess_module = Preprocessing()
    
    """
    Read Text Function, reads a text file according to the file path given as a string.
    """
    def read_text(self, text_path):
        if not text_path.endswith(".txt"):
            raise Exception("The file is not a .txt file") 
        file = open(text_path, "r", encoding="utf-8")
        content = file.read()
        if content == '':
            raise Exception("The file is empty")
        self.textToCompare = content
        file.close()
        return self.textToCompare

    """
    Preprocess Data Function, preprocesses the data of the saved text using the
    functions in the Preprocessing class.
    """
    def preprocess_data(self):
        self.preproccess_module.set_text(self.textToCompare)
        self.preproccess_module.preprocess_data()
        self.text_n_grams = self.preproccess_module.n_grams
        return self.text_n_grams

    """
    Get Similarity Score Function, calculates the similarity score between two 
    sentences according to their given list of n-grams. The score is calculated
    by dividing the number of n-grams that are present in both sentences by the
    total number of n-grams in both sentences. 
    """
    def get_similarity_score(self, sentence1_ngrams, sentence2_ngrams):
        if not sentence1_ngrams or not sentence2_ngrams:
            return 0
        set_sentence1 = set(sentence1_ngrams)
        set_sentence2 = set(sentence2_ngrams)
        ngrams_both = set_sentence1.intersection(set_sentence2)
        ngrams_list = set_sentence1.union(set_sentence2)
        score = len(ngrams_both) / len(ngrams_list)
        return round(score, 2)

    """
    Get Similarity Matrix Function, calculates the similarity matrix between two
    given paragraphs, using the similarity score function.
    """
    def get_similarity_matrix(self, paragraph1, paragraph2):
        similarities_matrix = []
        for sentence2 in paragraph2:
            sentence_similarity = []
            for sentence1 in paragraph1:
                score = self.get_similarity_score(sentence1, sentence2)
                sentence_similarity.append(score)
            similarities_matrix.append(sentence_similarity)
        return similarities_matrix

    """
    Compare Function, compares the text that was read and preprocessed with the
    texts in the dictionary, calculating the mean of each similarity matrix 
    between the analyzed text and each text from the dictionary. The function
    returns a boolean value that indicates if the text is plagiarized, the sum
    of the scores of the possible plagiarism and a list of the possible
    plagiarism texts.
    """
    def compare(self, text_path):
        try:
            self.read_text(text_path)
        except Exception as e:
            raise Exception(e)
        self.preprocess_data()
        possible_plagiarism_texts = []
        sum_scores = 0
        for key in self.dictionary:
            n_gram_scores = []
            n_gram_length_sum = 0
            final_score = 0
            for n_gram_index in range(len(self.text_n_grams)):
                original_text_ngrams = self.dictionary[key][n_gram_index]
                actual_text_ngrams = self.text_n_grams[n_gram_index]
                n_gram_length = len(actual_text_ngrams[0][0]) if actual_text_ngrams else 0
                similarities_matrix = self.get_similarity_matrix(original_text_ngrams, actual_text_ngrams)
                mean_score = 0
                for sentence in similarities_matrix:
                    sentence_score = max(sentence) if sentence else 0
                    mean_score += sentence_score
                mean_score = (mean_score / (len(similarities_matrix))) * n_gram_length if similarities_matrix else 0
                n_gram_length_sum += n_gram_length
                n_gram_scores.append(mean_score)
            final_score = round(sum(n_gram_scores) / n_gram_length_sum, 2)
            if final_score > 0.01:
                plagiarism_info = (key, final_score)
                possible_plagiarism_texts.append(plagiarism_info)
                sum_scores += final_score
        
        return (True, '{:.2f}'.format(sum_scores), possible_plagiarism_texts) if (sum_scores >= 0.05) else (False, '{:.2f}'.format(sum_scores), "No plagiarism detected", possible_plagiarism_texts)