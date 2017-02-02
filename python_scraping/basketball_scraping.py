#!/usr/bin/python

import urllib
import bs4 from BeautifulSoup

soup = BeautifulSoup('http://www.basketball-reference.com/teams/UTA/2017.html')

for players in soup.find_all('a')
    print players
