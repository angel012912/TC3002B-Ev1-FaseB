"""
Team 5
José Ángel García Gómez - A01745865
David Damian Galan - A01752785
Luis Humberto Romero Pérez - A01752789
File or class that contains all functions to calculate the similitude between two texts
"""

# Libraries
from Preprocessing import Preprocessing
from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences
import pickle
import random

class Compare:

    possible_plagiarism_types = ['active_passive', 'copy', 'different', 'paraphrase', 'tense']

    """
    Constructor for the class Compare, it initializes current text that is being analyzed
    an instance of the Preprocessing class, a given dictionary of texts to compare with
    and the list of n-grams of the text that is being analyzed.
    """
    def __init__(self, dictionary, model_path="", tokenizer_path="", max_sequence_length=80):
        self.textToCompare = ''
        self.dictionary = dictionary
        self.text_sentences = []
        self.preproccess_module = Preprocessing()
        try:
            if not model_path or not tokenizer_path:
                raise Exception("Model or tokenizer paths not found")
            model = self._load_model(model_path)
            tokenizer = self._load_tokenizer(tokenizer_path)
            self.compare_model = self._set_model(model)
            self.tokenizer = self._set_tokenizer(tokenizer, max_sequence_length)
        except Exception as e:
            print(e)
            self.compare_model = self._set_default_model
            self.tokenizer = self._set_default_tokenizer
    
    def _load_model(self, model_path):
        model = load_model(model_path)
        return model
    
    def _load_tokenizer(self, tokenizer_path):
        with open(tokenizer_path, "rb") as file:
            tokenizer = pickle.load(file)
        return tokenizer
    
    def _set_tokenizer(self, tokenizer, max_sequence_length=80):
        def tokenize(sentence, max_sequence_length=max_sequence_length, tokenizer=tokenizer):
          sequence = pad_sequences(tokenizer.texts_to_sequences([sentence]), maxlen=max_sequence_length)
          return sequence
        
        return tokenize

    def _set_model(self, model):
        def model_predict(sequence1, sequence2, model=model):
            prediction = model.predict([sequence1, sequence2])
            is_plagiarism = max(prediction[0][0])
            index_plagiarism_type = prediction[1][0].argmax()
            plagiarism_type = self.possible_plagiarism_types[index_plagiarism_type] if is_plagiarism else None
            return (is_plagiarism, plagiarism_type)

        return model_predict

    def _set_default_model(self, sentence1, sentence2):
        is_plagiarized = random.choice([0, 1])
        plagiarism_type = random.choice(self.possible_plagiarism_types) if is_plagiarized else None
        result = (is_plagiarized, plagiarism_type)
        return result

    def _set_default_tokenizer(self, sentence):
        return sentence
    
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
        self.text_sentences = self.preproccess_module.sentences
        return self.text_sentences

    """
    Get Similarity Score Function, calculates the similarity score between two 
    sentences according to their given list of n-grams. The score is calculated
    by dividing the number of n-grams that are present in both sentences by the
    total number of n-grams in both sentences. 
    """
    def get_similarity_score(self, sentence1, sentence2):
        if not sentence1 or not sentence2:
            return (0, None)
        sentence1_tokenized = self.tokenizer(sentence1)
        sentence2_tokenized = self.tokenizer(sentence2)
        result = self.compare_model(sentence1_tokenized, sentence2_tokenized)
        return result

    """
    Get Similarity Matrix Function, calculates the similarity matrix between two
    given paragraphs, using the similarity score function.
    """
    def get_similarity_matrix(self, paragraph1, paragraph2):
        similarities_matrix = []
        plagiarism_types_detecet = set()
        for sentence2 in paragraph2:
            sentence_similarity = []
            for sentence1 in paragraph1:
                score, plagiarism_type = self.get_similarity_score(sentence1, sentence2)
                plagiarism_types_detecet.add(plagiarism_type) if plagiarism_type else None
                sentence_similarity.append(score)
            similarities_matrix.append(sentence_similarity)
        return (similarities_matrix, list(plagiarism_types_detecet))

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
            sentence_scores = []
            final_score = 0
            original_text_sentences = self.dictionary[key]
            actual_text_sentences = self.text_sentences
            similarities_matrix, plagiarisms_detected = self.get_similarity_matrix(original_text_sentences, actual_text_sentences)
            mean_score = 0
            for sentence in similarities_matrix:
                sentence_score = max(sentence) if sentence else 0
                mean_score += sentence_score / len(sentence)
            mean_score = (mean_score / (len(similarities_matrix)))
            sentence_scores.append(mean_score)
            final_score = round(sum(sentence_scores) / len(sentence_scores), 2)
            if final_score > 0.01:
                plagiarism_info = (key, final_score, plagiarisms_detected)
                possible_plagiarism_texts.append(plagiarism_info)
                sum_scores += final_score
        
        return (True, '{:.2f}'.format(sum_scores), possible_plagiarism_texts) if (sum_scores >= 0.15) else (False, '{:.2f}'.format(sum_scores), "No plagiarism detected", possible_plagiarism_texts)
