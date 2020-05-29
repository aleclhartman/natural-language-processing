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
    
    # join stems to whitespace to return a cohesive string
    cohesive_stems = " ".join(stems)
    
    return stems, cohesive_stems

def lemmatize(string):
    """
    This function accepts a string and returns the string after applying lemmatization to each word.
    """
    
    # create lemmatizer object
    wnl = nltk.stem.WordNetLemmatizer()
    
    # use lemmatizer to generate list of stems
    lemmas = [wnl.lemmatize(word) for word in string.split()]
    
    # join lemmas to whitespace to return a cohesive string
    cohesive_lemmas = " ".join(lemmas)
    
    return lemmas, cohesive_lemmas

def remove_stopwords(lemmas_or_stems, extra_stopwords=[], exclude_stopwords=[]):
    """
    This function accepts a list of strings (lemmas_or_stems) and returns a string after removing stopwords.
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
    lemmas_or_stems_sans_stopwords = [word for word in lemmas_or_stems if word not in stopword_list]
    
    # join lemmas_or_stems_sans_stopwords to whitespace to return a cohesive string
    string_sans_stopwords = " ".join(lemmas_or_stems_sans_stopwords)
    
    return string_sans_stopwords

def prep_article(dictionary, key):
    """
    This function accepts a dictionary representing a singular article containing a body of text, as specified 
    in the key parameter, to clean. 
    The function then returns a dictionary containing the stemmed, lemmatized, and cleaned text in their 
    respective columns.
    """
    
    # indexing the original content
    content = dictionary[key]
    
    # running basic_clean function on content
    content = basic_clean(content)
    
    # running tokenize function on content
    content = tokenize(content)
    
    # running stem function on content
    stem_list, stem_string = stem(content)
    
    # creating stemmed column in df
    dictionary["stemmed"] = stem_string
    
    # running lemmatize function on content
    lemma_list, lemma_string = lemmatize(content)
    
    # creating lemmatized column in df
    dictionary["lemmatized"] = lemma_string
    
    # running remove_stopwords on lemma_list
    cleaned_content = remove_stopwords(lemma_list)
    
    # creating cleaned column in df
    dictionary["clean"] = cleaned_content
    
    return dictionary

def prepare_article_data(list_of_dictionaries):
    """
    This function accepts a list of dictionaries and returns a list of dictionaries after applying the 
    prep_article function to each article in the orignial dictionary.
    """
    
    # list comprehension applying prep_article function to each dictionary
    list_of_dictionaries = [prep_article(dictionary) for dictionary in list_of_dictionaries]
    
    return list_of_dictionaries