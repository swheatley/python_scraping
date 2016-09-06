from urllib.request import urlopen
from bs4 import BeautifulSoup


def getTitle(url):
    try:
        html = urlopen(url)
    # if html is None:
    # print("URL is not found")
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), "lxml")
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title
title = getTitle("http://www.pythonscraping.com/pages/page1.html")
if title is None:
    print("Title could not be found")
else:
    print(title)
