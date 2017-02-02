#!/usr/bin/env python

import urllib
import urllib2
from lxml import etree
import StringIO


result = urllib.urlopen("http://www.slcolibrary.org/")
html = result.read()


parser = etree.HTMLParser()
tree = etree.parse(StringIO.StringIO(html), parser)

href_xpath = "//*[@id='main-nav']/li/a/@href"

filtered_html = tree.xpath(href_xpath)

print filtered_html

links = [html for html in filtered_html if 'htm' in html]
print links

for link in links:
    main_page = urllib.urlopen("http://www.slcolibrary.org%s" % link)
    main_page_html = main_page.read()
    tree = etree.parse(StringIO.StringIO(main_page_html),parser)

    fantasy_xpath = "//*[@id='content']/div/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/ul/li[2]/a/@href"
    fantasy_string = tree.xpath(fantasy_xpath)

    print fantasy_string 