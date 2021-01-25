#BASIC LIBRARIES
import pandas as pd 
import numpy as np



# Defining a function to remove stop words, urls and symbols etc.

import nltk
import re, string
from string import punctuation
#nltk.download('punkt')
# this 
from nltk.tokenize import punkt
from nltk.tokenize import word_tokenize
from nltk import sent_tokenize
#nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer


# def gettext(message):
#     text = BeautifulSoup(message, 'html.parser')
#     return text.get_text()

def removehurls(message):
    return re.sub(r'http\S+', '', message)

def removesymbols(message):
    re.sub(r'^\x00-\x7F+', '', message)
    return re.sub('[@!.,\/&)?:#...-'']', '', message)

def removestopwords(message):
    new_message = []
    message = message.lower()
    message = word_tokenize(message)
    sw = stopwords.words('english')
    for msg in message:
        if msg not in sw:
            new_message.append(msg) 
    return ' '.join(new_message)

def preparemessage(message):
    # message = gettext(message)
    message = removehurls(message)
    message = removesymbols(message)
    message = removestopwords(message)
    return message


