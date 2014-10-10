from __future__ import print_function
import urllib2
from bs4 import BeautifulSoup


f = open('ListEnWikiVital100.txt','w')

urls = ['http://en.wikipedia.org/wiki/Wikipedia:Vital_articles/Level/2']

#pulls the article links to the vital 100, plus some misc. links

for url in urls:
	s = urllib2.urlopen(url).read()


	#with file('List of articles every Wikipedia should have_Expanded - Meta.html') as f:
	#    s = f.read()

	soup = BeautifulSoup(s)
	soup.prettify()


	for anchor in soup.findAll('a', href=True):
		if '/wiki/' in anchor['href'] and not ':' in anchor['href'] and not '//' in anchor['href'] and not 'Main_Page' in anchor['href']:  # keeps the links mostly limited to Wikipedia articles
			print(anchor['href'],file=f)

f.close