from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html, "lxml")

nameList = bsObj.findAll("span", {"class":"green"})
for name in nameList:
    print(name.get_text())


anotherList = bsObj.findAll(text="the prince")
print(len(anotherList))

allText = bsObj.findAll(id="text")
print(allText[0].get_text())
