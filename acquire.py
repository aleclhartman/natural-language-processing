import numpy as np
import pandas as pd

from requests import get
from bs4 import BeautifulSoup
import os

def get_blog_articles(urls=[]):
    """
    This function takes the list of urls passed into the function and returns a list of dictionaries,
    with each dictionary representing one article.
    """
    
    # creating list of dictionaries
    list_of_dicts = []
    
    # establish headers
    headers = {"User-Agent": "Codeup Data Science"}
    
    # iterate over list of urls
    for url in urls:
        
        # get response from url
        response = get(url, headers=headers)

        # create soup object
        soup = BeautifulSoup(response.content, "html.parser")

        # create title object
        title = soup.title.string

        # create content object
        content = soup.find("div", class_="jupiterx-post-content clearfix")

        # make the article more legible
        content = content.text

        # creating dictionary
        dictionary = {
            "title": title,
            "content": content
        }

        # appending dictionaries to list
        list_of_dicts.append(dictionary)
    
    df = pd.DataFrame(list_of_dicts)
    
    return df

def get_news_articles(categories=[]):
    """
    This function takes the list of categories passed into the function and returns a list of dictionaries,
    with each dictionary representing one article.
    """
    
    # create empty list to append to later
    list_of_articles = []
    
    # iterate over the list of categories passed into the function
    for category in categories:
        
        # navigate to the category page
        url = "https://inshorts.com/en/read/" + category
        
        # establish headers
        headers = {"User-Agent": "Codeup Data Science"}
        
        # get response from url
        response = get(url, headers=headers)
        
        # create soup object
        soup = BeautifulSoup(response.content, "html.parser")
        
        # create articles object
        articles = soup.select(".news-card")
        
        # iterate over articles
        for article in articles:
            
            # select title of article
            title = article.select("span[itemprop='headline']")[0].text
            
            # select body of article
            body = article.select("div[itemprop='articleBody']")[0].text
            
            # create dictionary containing title, body, and category of article
            dictionary = {
                "title": title,
                "content": body,
                "category": category
            }
            
            # append dictionary to list
            list_of_articles.append(dictionary)
            
        df = pd.DataFrame(list_of_articles)

    return df