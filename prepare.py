import numpy as np
import pandas as pd

import unicodedata
import re
import json

import nltk
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.corpus import stopwords

import acquire as ac

def basic_clean(string):
    """
    This function accepts a string and returns the string after applying some basic text cleaning to each word.
    """
    
    # lowercase all characters
    string = string.lower()
    
    # normalize unicode characters
    string = unicodedata.normalize("NFKD", string)\
                .encode("ascii", "ignore")\
                .decode("utf-8", "ignore")
    
    # replace anything that is not a letter, number, whitespace or a single quote.
    string = re.sub(r"[^a-z0-9\s']", "", string)
    
    return string

def tokenize(string):
    """
    This function accepts a string and returns the string after tokenizing to each word.
    """
    
    # make tokenizer object
    tokenizer = ToktokTokenizer()

    # use tokenizer object and return string
    string = tokenizer.tokenize(string, return_str=True)
    
    return string

def stem(string):
    """
    This function accepts a string and returns the string after applying stemming to each word.
    """
    
    # create stemmer object
    ps = nltk.porter.PorterStemmer()
    
    # use stemmer to generate list of stems
    stems = [ps.stem(word) for word in string.split()]
    
    # join stems to whitespace to return cohesive string
    cohesive_stems = " ".join(stems)
    
    return cohesive_stems

def lemmatize(string):
    """
    This function accepts a string and returns the string after applying lemmatization to each word.
    """
    
    # create lemmatizer object
    wnl = nltk.stem.WordNetLemmatizer()
    
    # use lemmatizer to generate list of stems
    lemmas = [wnl.lemmatize(word) for word in string.split()]
    
    # join stems to whitespace to return cohesive string
    cohesive_lemmas = " ".join(lemmas)
    
    return cohesive_lemmas

