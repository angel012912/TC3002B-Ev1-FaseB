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
import numpy as np

class Compare:

    POSSIBLE_PLAGIARISM_TYPES = ['active_passive', 'copy', 'different', 'paraphrase', 'tense']

    def __init__(self, dictionary, model_path="", tokenizer_path="", max_sequence_length=80):
        """
        Initializes the object with the provided parameters.

        Args:
            dictionary (dict): The dictionary used for comparison.
            model_path (str, optional): The path to the comparison model file. Defaults to "".
            tokenizer_path (str, optional): The path to the tokenizer file. Defaults to "".
            max_sequence_length (int, optional): The maximum sequence length for tokenization. Defaults to 80.

        Attributes:
            textToCompare (str): Holds the text to compare.
            dictionary (dict): The dictionary used for comparison.
            text_sentences (list): A list to store sentences extracted from text.
            preproccess_module (Preprocessing): An instance of Preprocessing class.
            compare_model (Model): The loaded comparison model.
            tokenizer (Tokenizer): The loaded tokenizer.

        Raises:
            Exception: If model_path or tokenizer_path are not provided.

        Example:
            Initialize the object with a dictionary and model files:
            comparer = Comparer(dictionary, model_path='model.h5', tokenizer_path='tokenizer.pickle')
        """
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
        """
        Loads the comparison model from the provided path.

        Args:
            model_path (str): The path to the comparison model file.

        Returns:
            Model: The loaded comparison model.

        Example:
            model = self._load_model('model.bin')
        """
        model = load_model(model_path)
        return model
    
    def _load_tokenizer(self, tokenizer_path):
        """
        Loads the tokenizer from the provided path.

        Args:
            tokenizer_path (str): The path to the tokenizer file.

        Returns:
            Tokenizer: The loaded tokenizer.

        Example:
            tokenizer = self._load_tokenizer('tokenizer.bin')
        """
        with open(tokenizer_path, "rb") as file:
            tokenizer = pickle.load(file)
        return tokenizer
    
    def _set_tokenizer(self, tokenizer, max_sequence_length=80):
        """
        Loads the tokenizer from the provided path.

        Args:
            tokenizer_path (str): The path to the tokenizer file.

        Returns:
            Tokenizer: The loaded tokenizer.

        Example:
            tokenizer = self._load_tokenizer('tokenizer.bin')
        """
        def tokenize(sentence, max_sequence_length=max_sequence_length, tokenizer=tokenizer):
          if type(sentence) == str:
              sentence = [sentence]
          sequence = pad_sequences(tokenizer.texts_to_sequences(sentence), maxlen=max_sequence_length)
          return sequence
        
        return tokenize

    def _set_model(self, model):
        """
        Sets up the model prediction function for comparing sentences.

        Args:
            model (Model): The loaded comparison model.

        Returns:
            function: A function for predicting plagiarism.

        Example:
            predict_func = self._set_model(model)
            prediction = predict_func(sequence1, sequence2)
        """
        def model_predict(sequence1, sequence2, model=model):
            prediction = model.predict([sequence1, sequence2], verbose=0)
            is_plagiarism_list = np.array(prediction[0])
            predicted_classes_list = list(map(lambda x: self.POSSIBLE_PLAGIARISM_TYPES[x], np.argmax(prediction[1], axis=1)))
            return (is_plagiarism_list, predicted_classes_list)

        return model_predict

    def _set_default_model(self, sentence1, sentence2):
        """
        Sets up the default model function for generating random plagiarism predictions.

        Args:
            sentence1 (str): First sentence.
            sentence2 (str): Second sentence.

        Returns:
            tuple: A tuple containing plagiarism prediction.

        Example:
            prediction = self._set_default_model('Sentence 1', 'Sentence 2')
        """
        is_plagiarized = random.choice([0, 1])
        plagiarism_type = random.choice(self.POSSIBLE_PLAGIARISM_TYPES) if is_plagiarized else None
        result = (is_plagiarized, plagiarism_type)
        return result

    def _set_default_tokenizer(self, sentence):
        """
        Sets up the default tokenizer function that returns the input sentence as is.

        Args:
            sentence (str): Input sentence.

        Returns:
            str: The input sentence.

        Example:
            tokenized_sentence = self._set_default_tokenizer('Sample sentence')
        """
        return sentence
    
    def read_text(self, text_path):
        """
        Read Text Function, reads a text file according to the file path given as a string.
        """
        if not text_path.endswith(".txt"):
            raise Exception("The file is not a .txt file") 
        file = open(text_path, "r", encoding="utf-8")
        content = file.read()
        if content == '':
            raise Exception("The file is empty")
        self.textToCompare = content
        file.close()
        return self.textToCompare

    def preprocess_data(self):
        """
        Preprocess Data Function, preprocesses the data of the saved text using the
        functions in the Preprocessing class.
        """
        self.preproccess_module.set_text(self.textToCompare)
        self.preproccess_module.preprocess_data()
        self.text_sentences = self.preproccess_module.sentences
        return self.text_sentences

    def get_similarity_score(self, sentence1, sentence2):
        """
        Calculates the similarity score between two sentences.

        Args:
            sentence1 (str): First sentence.
            sentence2 (str): Second sentence.

        Returns:
            tuple: A tuple containing the similarity score and plagiarism type.

        Example:
            similarity_score = self.get_similarity_score('Sentence 1', 'Sentence 2')
        """
        if not sentence1 or not sentence2:
            return (0, None)
        sentence1_tokenized = self.tokenizer(sentence1)
        sentence2_tokenized = self.tokenizer(sentence2)
        result = self.compare_model(sentence1_tokenized, sentence2_tokenized)
        return result

    def get_similarity_matrix(self, paragraph1, paragraph2):
        """
        Generates a similarity matrix between two paragraphs.

        Args:
            paragraph1 (list): List of sentences in the first paragraph.
            paragraph2 (list): List of sentences in the second paragraph.

        Returns:
            tuple: A tuple containing the similarity score matrix and plagiarism types.

        Example:
            similarity_matrix, plagiarism_types = self.get_similarity_matrix(paragraph1, paragraph2)
        """
        array_sequence2 = []
        array_sequence1 = []
        for sentence2 in paragraph2:
            for sentence1 in paragraph1:
                array_sequence1.append(sentence1)
                array_sequence2.append(sentence2)
        score_list, plagiarism_type_list = self.get_similarity_score(array_sequence1, array_sequence2)
        plagiarism_type_list = set(plagiarism_type_list)
        if self.POSSIBLE_PLAGIARISM_TYPES[2] in plagiarism_type_list:
            plagiarism_type_list.remove(self.POSSIBLE_PLAGIARISM_TYPES[2])
        score_list = score_list.reshape(len(paragraph2), len(paragraph1))
        return (score_list, list(plagiarism_type_list))

    def compare(self, text_path):
        """
        Compares the text with the provided dictionary.

        Args:
            text_path (str): The path to the text file.

        Returns:
            tuple: A tuple containing the result of the comparison.

        Raises:
            Exception: If there's an error reading the text or preprocessing the data.

        Example:
            result = self.compare('text.txt')
        """
        try:
            self.read_text(text_path)
        except Exception as e:
            raise Exception(e)
        self.preprocess_data()
        possible_plagiarism_texts = []
        sum_scores = 0
        for key in self.dictionary:
            final_score = 0
            original_text_sentences = self.dictionary[key]
            actual_text_sentences = self.text_sentences
            similarities_matrix, plagiarisms_detected = self.get_similarity_matrix(original_text_sentences, actual_text_sentences)
            sum_score = 0
            for sentence in similarities_matrix:
                if len(sentence) == 0:
                    mean_score += 0
                    continue
                sentence_score = max(sentence)
                sum_score += sentence_score
            final_score = (sum_score / (len(similarities_matrix)))
            final_score = round(final_score, 2)
            if final_score >= 0.2:
                plagiarism_info = (key, final_score, plagiarisms_detected)
                possible_plagiarism_texts.append(plagiarism_info)
                sum_scores += final_score
        
        return (True, '{:.2f}'.format(sum_scores), possible_plagiarism_texts) if (sum_scores >= 0.45) else (False, '{:.2f}'.format(sum_scores), "No plagiarism detected", possible_plagiarism_texts)
