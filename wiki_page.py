import requests
from bs4 import BeautifulSoup

# GOAL:
# open a wikipedia article,
# find the first link in the article,
# follow the link,
# repeat until the desired page is reached or an article loops to a previous article
# plot the distribution of attempts

# connect to a webpage and store the response in a variable called response,
# response.text is the actual string that is returned
response = requests.get("https://en.wikipedia.org")
html = response.text

# create a soup object which is easier to work with than pure html
soup = BeautifulSoup(html, 'html.parser')

# main loop
def continue_crawl(search_history, target_url, max_steps=25):
    if search_history[-1] == target_url:
        print("We've found the target article!")
        return False
    elif len(search_history) > max_steps:
        print("The search has gone on suspiciously long, aborting search!")
        return False
    elif search_history[-1] in search_history[:-1]:
        print("We've arrived at an article we've already seen, aborting search!")
        return False
    else:
        return True