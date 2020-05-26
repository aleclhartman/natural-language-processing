from requests import get
from bs4 import BeautifulSoup
import os

def get_blog_articles(urls=[]):
    """
    This function takes the list of urls passed into the function and returns a list of dictionaries,
    with each dictionary representing one article."""
    
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

        # create article object
        article = soup.find("div", class_="jupiterx-post-content clearfix")

        # make the article more legible
        article = article.text

        # creating dictionary
        dictionary = {
            "title": title,
            "article": article
        }

        # appending dictionaries to list
        list_of_dicts.append(dictionary)
    
    return list_of_dicts