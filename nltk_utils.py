import nltk
from nltk.tokenize import sent_tokenize
import nltk.data

#nltk.download('punkt')
#tokenizer= nltk.data.load("tokenizers/punkt/spanish.pickle")

#from nltk.stem.porter import PorterStemmer
#stemmer = PorterStemmer()

from nltk.stem import SnowballStemmer
stemmer = SnowballStemmer('spanish')

def tokenizer(sentence):
    return nltk.word_tokenize(sentence)
    #print (tokenizer.tokenize(sentence))

def stem(word):
    return stemmer.stem(word.lower())

def bag_of_words(tokenized_sentence,all_words):
    pass

