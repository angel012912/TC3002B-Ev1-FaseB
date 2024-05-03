"""
Team 5
José Ángel García Gómez - A01745865
David Damian Galan - A01752785
Luis Humberto Romero Pérez - A01752789
File or class that contains all preprocessing functions for the tool
"""

# Libraries
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.util import ngrams


class Preprocessing:
    
    def __init__(self):
        """
        Constructor for the class Preprocessing, with the corresponding attributes and
        the instance of the WordNetLemmatizer class.
        """
        self.current_text = ''
        self.processed_text = ''
        self.sentences = []
        self.word_list = []
        self.lemmatizer = WordNetLemmatizer()
    
    def set_text(self, text):
        """
        Set Text Function, sets the current text that is being processed to the text
        given as a string.
        """
        self.current_text = text
        return self.current_text

    def to_lower_without_punctuation(self):
        """
        Text cleaning function, removes punctuation (except final stops) and converts 
        all characters to lowercase in the current text variable.
        """
        final_headline = ""
        for c in self.current_text:
            if (c >= 'a' and c <= 'z') or c == ' ' or (c >= 'A' and c <= 'Z') or c == '.':
                final_headline += c
        self.current_text = final_headline.lower()
        return self.current_text

    def sentence_separation(self):
        """
        Sentence Separation Function, separates the current text into a list of sentences
        """
        self.sentences = list(filter(lambda x: x.strip(), self.current_text.split('.')))
        return self.sentences
    
    def stopword_removal(self):
        """
        Stopword Removal Function, removes stopwords from the sentences list of the
        processed text.
        """
        stop_words = set(stopwords.words('english'))
        self.word_list = []
        for sentence in self.sentences:
            word_tokens = word_tokenize(sentence)
            filtered_sentence = [w for w in word_tokens if not w in stop_words]
            self.word_list.append(filtered_sentence)
        return self.word_list

    def lemmatize_words(self):
        """
        Lemmatize Words Function, lemmatizes the words in the word list of the processed
        text.
        """
        self.word_list = [[self.lemmatizer.lemmatize(word) for word in sentence] for sentence in self.word_list]
        return self.word_list

    def recreate_sentences(self):
        """
        Recreates sentences from a list of words and assigns them to the 'sentences' attribute.

        This method assumes that 'self.word_list' is a list of lists, where each inner list
        contains words representing a sentence.

        Returns:
            list: A list containing the recreated sentences.

        Example:
            If self.word_list = [['Hello', 'world'], ['This', 'is', 'a', 'sentence']]:
            Then self.sentences will be ['Hello world', 'This is a sentence'].
        """
        self.sentences = [' '.join(sentence) for sentence in self.word_list]
        return self.sentences
    
    def preprocess_data(self):
        """
        Preprocess Data Function, preprocesses the data of the current text using the
        functions of the rest of the class. N-grams are defined from 2 to 6.
        """
        self.sentence_separation()
        return self.sentences