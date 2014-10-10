from __future__ import print_function
import urllib2, urllib
from bs4 import BeautifulSoup, Comment
import time
import os


def downloadWikiArticle(url):
	link = urllib.unquote(url).decode('utf8').strip()
	url = 'http://en.wikipedia.org'+url


	articleName = link.replace('/wiki/','').strip()
	articleName = articleName.encode('utf-8')
	print(articleName)

	s = urllib2.urlopen(url).read()

	
	try:
		f = open('./wiki/liveArticles/'+articleName+'.html','w')
		print(s,file=f)
		f.close
		time.sleep(0.5)  # to be nice to Wikipedia's servers
	except:
		pass


with open('lists/ListEnWikiVital.txt','r') as f:
	i=0
	for line in f:
		i+=1

		print('Article #'+str(i))
		articleName = urllib.unquote(line).decode('utf8').strip()
		articleName = articleName.replace('/wiki/','').strip()
		articleName = articleName.encode('utf-8')
		#print('./wiki/liveArticles/'+articleName+'.html')
		if os.path.isfile('./wiki/liveArticles/'+articleName+'.html'):
			print(articleName+' already downloaded')  # in case the script gets interrupted, we don't want to re-download already acquired files
		else:
			downloadWikiArticle(line)

        


