# In[9]:

import time
import datetime
import random
import requests

import tweepy
from bs4 import BeautifulSoup


# In[10]:


CONSUMER_KEY = 'API Key'
CONSUMER_SECRET = 'API Key Secret'
ACCESS_KEY = 'Access Token'
ACCESS_SECRET = 'Access Token Secret'
BEARER_TOKEN = 'Your Bearer Token'

auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY,ACCESS_SECRET)
api = tweepy.API(auth)


# In[11]:


try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")


# In[12]:


def pullQuote():
    quoteLength = 999
    tweetText = ''
    
    while (quoteLength > 280):
        # The page we want to scrape. Tests connection
        pageNum = random.randint(1, 10)
        page = requests.get("https://quotes.toscrape.com/page/" + str(pageNum))

        # Get the HTML content and find all instances where class is quote
        soup = BeautifulSoup(page.content, 'html.parser')
        quotes = soup.find_all(class_="quote")

        # Each page has 10 quotes, generate a random value in this range and pull the quote
        randInt = random.randint(0, 9)

        quoteText = quotes[randInt].find_all(class_="text")[0].text     # Get the quote from the inner class
        quoteAuthor = quotes[randInt].find_all(class_="author")[0].text # Get the Author from the inner class
        
#         tweetText = (quoteText + '\n' + quoteAuthor + '\n' + page.url)
        tweetText = (quoteText + '\n' + quoteAuthor)   # No URL in tweet

        quoteLength = len(tweetText)

    return(tweetText)


# In[13]:


def makeTweet(message):
  api.update_status(message)


# In[14]:


def autoTweet():
  while True:
    message = pullQuote()
    makeTweet(message)
    print('Tweet Created: ' + str(datetime.datetime.now()))
#     time.sleep (43200)        # wait 12 hours before creating another tweet
    time.sleep (3600)        # wait 1 hours before creating another tweet


# In[15]:


def main():
  autoTweet()


# In[16]:


main()

