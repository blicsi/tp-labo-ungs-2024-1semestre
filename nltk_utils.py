import nltk
from nltk.tokenize import sent_tokenize
import nltk.data
import numpy as np

#nltk.download('punkt')
#tokenizer= nltk.data.load("tokenizers/punkt/spanish.pickle")

from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()

#from nltk.stem import SnowballStemmer
#stemmer = SnowballStemmer('spanish')

def tokenize(sentence):
    return nltk.word_tokenize(sentence)
    #print (tokenizer.tokenize(sentence))

def stem(word):
    return stemmer.stem(word.lower())

def bag_of_words(tokenized_sentence,all_words):
    tokenized_sentence=[stem(w) for w in tokenized_sentence]

    bag = np.zeros(len(all_words),dtype=np.float32)
    for idx, w in enumerate(all_words):
        if w in tokenized_sentence:
            bag[idx]=1.0
    return bag
