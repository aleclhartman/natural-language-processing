import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

import unicodedata

import re

import nltk
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.corpus import stopwords

import acquire as ac
import prepare as pr

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
    string = re.sub(r"[^a-z0-9\s]", "", string)
    
    return string

def tokenize(string):
    """
    This function accepts a string and returns a list of tokens after tokenizing to each word.
    """
    
    # make tokenizer object
    tokenizer = ToktokTokenizer()

    # use tokenizer object and return string
    list_of_tokens = tokenizer.tokenize(string, return_str=False)
    
    return list_of_tokens

def lemmatize(list_of_tokens):
    """
    This function accepts a list of tokens and returns a list after applying lemmatization to each word.
    """
    
    # create lemmatizer object
    wnl = nltk.stem.WordNetLemmatizer()
    
    # use lemmatizer to generate list of stems
    lemmas = [wnl.lemmatize(word) for word in list_of_tokens]
    
    # join lemmas to whitespace to create a cohesive string
    cohesive_lemmas = " ".join(lemmas)
    
    return lemmas

def remove_stopwords(lemmas, extra_stopwords=[], exclude_stopwords=[]):
    """
    This function accepts a list of strings (lemmas) and returns a list after removing stopwords.
    Extra words can be added the standard english stopwords using the extra_stopwords parameter.
    Words can be excluded from the standard english stopwords using the exclude_stopwords parameter.
    """
    
    # create stopword list
    stopword_list = stopwords.words("english")
    
    # extend extra_stopwords variable to stopwords if there are words in the parameter
    if not extra_stopwords:
        stopword_list
    else:
        stopword_list.extend(extra_stopwords)
    
    # remove words in exclude_stopwords variable from stopwords if there are words in the parameter
    if not exclude_stopwords:
        stopword_list
    else:
        stopword_list = [word for word in stopword_list if word not in exclude_stopwords]
    
    # list comprehension 
    lemmas_sans_stopwords = [word for word in lemmas if word not in stopword_list]
    
    return lemmas_sans_stopwords

def clean(text, extra_stopwords=[]):
    """
    A simple function to cleanup text data.
    This function is adapted from Zach Gulde's function from the NLP explore lesson using the functions
    I made in the NLP prepare exercises.
    """
    
    # call basic_clean function on text
    text = basic_clean(text)
    
    # call tokenize function on text
    list_of_tokens = tokenize(text)
    
    # call lemmatize function on list_of_tokens
    lemmas = lemmatize(list_of_tokens)
    
    # call remove_stopwords with extra_stopwords on lemmas
    lemmas_sans_stopwords = remove_stopwords(lemmas, extra_stopwords=extra_stopwords)
    
    return lemmas_sans_stopwords