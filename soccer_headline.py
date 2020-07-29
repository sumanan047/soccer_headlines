#Total package here enerating top 10 soccer headlines from ESPN, write a pakage

# list of dependecy packages
import bs4
from bs4 import BeautifulSoup
import urllib.request  
import re

# required utility functions 
# get_byte_from_url takes a url and returns bytes
def get_bytes_from_url(url):
    html=urllib.request.urlopen(url).read()
    return html

#global variable url takes the homepage url of espn soccernet to scare the top webnews from their website
url = "https://www.espn.com/soccer/"

# soup then returns a beautiful soup object which is then parsed using regular expression to get the top 10 hadlines in soccer. 
soup = BeautifulSoup(get_bytes_from_url(url),features="html.parser")
#print(soup.prettify())


gem=soup.find_all(href=re.compile("story"), class_="")
#print(gem[29].get_text())
# this works but how do you split the news healdines

def get_headlines():
    print("TOP 10 SOCCER HEADLINES RIGHT NOW!")
    for i in range(10):
        print("Headline",i+1)
        print(gem[i].get_text())