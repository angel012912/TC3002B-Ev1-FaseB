# Team 5
# José Ángel García Gómez - A01745865
# David Damian Galan - A01752785
# Luis Humberto Romero Pérez - A01752789
# File or class that contains all preprocessing functions for the tool
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.util import ngrams


class Preprocessing:
    
    # Constructor for the class Preprocessing, with the corresponding attributes and
    # the instance of the WordNetLemmatizer class.
    def __init__(self):
        self.current_text = ''
        self.processed_text = ''
        self.sentences = []
        self.word_list = []
        self.n_grams = []
        self.lemmatizer = WordNetLemmatizer()
    
    # Set Text Function, sets the current text that is being processed to the text
    # given as a string.
    def set_text(self, text):
        self.current_text = text
        return self.current_text

    # Text cleaning function, removes punctuation (except final stops) and converts 
    # all characters to lowercase in the current text variable.
    def to_lower_without_punctuation(self):
        final_headline = ""
        for c in self.current_text:
            if (c >= 'a' and c <= 'z') or c == ' ' or (c >= 'A' and c <= 'Z') or c == '.':
                final_headline += c
        self.current_text = final_headline.lower()
        return self.current_text
    
    # Sentence Separation Function, separates the current text into a list of sentences
    def sentence_separation(self):
        self.sentences = list(filter(lambda x: x.strip(), self.current_text.split('.')))
        return self.sentences
    
    # Stopword Removal Function, removes stopwords from the sentences list of the
    # processed text.
    def stopword_removal(self):
        stop_words = set(stopwords.words('english'))
        self.word_list = []
        for sentence in self.sentences:
            word_tokens = word_tokenize(sentence)
            filtered_sentence = [w for w in word_tokens if not w in stop_words]
            self.word_list.append(filtered_sentence)
        return self.word_list

    # Lemmatize Words Function, lemmatizes the words in the word list of the processed
    # text.
    def lemmatize_words(self):
        self.word_list = [[self.lemmatizer.lemmatize(word) for word in sentence] for sentence in self.word_list]
        return self.word_list

    # Create N-Grams Function, creates n-grams of the word list of the 
    # sentences from the processed text, given the range of the n-grams.
    def create_n_grams(self, n_range):
        self.n_grams = []
        for n in n_range:
            ngram_list = []
            for sentence in self.word_list:
                sentence_n_grams = []
                for i in range(len(sentence)-n+1):
                    sentence_n_grams.append(tuple(sentence[i:i+n]))
                ngram_list.append(sentence_n_grams) if sentence_n_grams else None
            self.n_grams.append(ngram_list)
        return self.n_grams
    
    # Preprocess Data Function, preprocesses the data of the current text using the
    # functions of the rest of the class. N-grams are defined from 2 to 6.
    def preprocess_data(self):
        self.to_lower_without_punctuation()
        self.sentence_separation()
        self.stopword_removal()
        self.lemmatize_words()
        self.create_n_grams(range(2, 6))
        return self.n_grams