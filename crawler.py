# searchengine.py
#
# From: Programming Collective Intelligence - Toby Segaran
#
# Usage:
# >>> from crawler import crawler
# >>> pagelist = ['http://nl.wikipedia.org']
# >>> crawler = crawler.crawler('')
# >>> crawler.crawl(pagelist)

# runable from python 2 and python 3
from __future__ import print_function

try:
    input = raw_input
except:
    pass

import requests
try:
    from urllib.parse import urljoin # python3
except ImportError:
    from urlparse import urljoin # python2
from bs4 import *

# Create a list of words to ignore
ingorewords = {'the', 'of', 'to', 'and', 'a', 'in', 'is', 'it'}

class crawler:
    # Initialize the crawler with the name of database
    def __init__(self, dbname):
        pass

    def __del__(self):
        pass

    def dbcommit(self):
        pass

    # Auxilliary function for getting an entry id and adding
    # it if it's not present
    def getentryid(self, table, field, value, createnew = True):
        return None

    # Index an individual page
    def addtoindex(self, url, soup):
        print('Indexing %s' % url)

    # Extract the text from an HTML page (no tags)
    def gettextonly(self, soup):
        return None

    # Separate the words by any non-whitespace character
    def separatewords(self, text):
        return None

    # Return true if this url is already indexed
    def isindexed(self, url):
        return False

    # Add a link between two pages
    def addlinkref(self, urlFrom, urlTo, linkText):
        pass

    def search_term_found(self, search_term, url):
        print('   > "' + search_term + '" found in ' + url)

    # Starting with a list of pages, do a breadth
    # first search to the given depth, indexing pages
    # as we go
    def crawl(self, pages, depth = 2, search_term = None):
        for i in range(depth):
            newpages = set()
            for page in pages:
                try:
                    c = requests.get(page)
                except:
                    print('Could not open %s' % page)
                    continue
                soup = BeautifulSoup(c.text, 'html.parser')
                self.addtoindex(page, soup)

                if search_term and search_term in soup.text:
                    self.search_term_found(search_term, page)

                links = soup('a')
                for link in links:
                    if ('href' in dict(link.attrs)):
                        url = urljoin(page, link['href'])
                        if url.find("'") != -1: continue
                        if url.find(".jpg") != -1: continue
                        url = url.split('#')[0] # remove location portion
                        if url[0:4] == 'http' and not self.isindexed(url):
                            newpages.add(url)
                        linkText = self.gettextonly(link)
                        self.addlinkref(page, url, linkText)

                self.dbcommit()

            pages = newpages

    # Create the database tables
    def createindextables(self):
        pass

# ---------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':

    search_term = input("Give search term: ")

    try:
        c = crawler('')
        c.crawl(['http://www.nu.nl'], search_term = search_term)

    except KeyboardInterrupt:
        print('stopped')