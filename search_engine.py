# searchengine.py
#
# From: Programming Collective Intelligence - Toby Segaran
#
# Usage:
# >>> import searchengine
# >>> pagelist = ['http://nl.wikipedia.org']
# >>> crawler = searchengine.crawler('')
# >>> crawler.crawl(pagelist)

from urllib.request import urlopen
from urllib.parse import urljoin
from bs4 import *

# Create a list of words to ignore
ingorewords = set(['the', 'of', 'to', 'and', 'a', 'in', 'is', 'it'])

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

    # Starting with a list of pages, do a breadth
    # first search to the given depth, indexing pages
    # as we go
    def crawl(self, pages, depth = 2):
        for i in range(depth):
            newpages = set()
            for page in pages:
                try:
                    c = urlopen(page)
                except:
                    print('Could not open %s' % page)
                    continue
                soup = BeautifulSoup(c.read(), 'html.parser', from_encoding='iso-8859-1')
                self.addtoindex(page, soup)

                links = soup('a')
                for link in links:
                    if ('href' in dict(link.attrs)):
                        url = urljoin(page, link['href'])
                        if url.find("'") != -1: continue
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

    try:
        c = crawler('')
        c.crawl(['http://www.nu.nl'])

    except KeyboardInterrupt:
        print('stopped')