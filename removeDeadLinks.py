# Python script that parses through static Wiki HTML and strips links to pages not within the static collection

from __future__ import print_function
from bs4 import BeautifulSoup, Comment
import os
import glob

liveFileDir = '/wiki/liveArticles/'  # dir of your live Wikipedia articles downloaded from scrapeWikiVital.py
staticFileDir = '/VOLUMES/LIBRARYBOX/static-Wikipedia-100'  # dir of where you want the static copies of the Wikipedia articles
mediaFileDir = staticFileDir+'/wiki/en/'  # the static articles will be placed within a /wiki/en/ for the English versions


def removeDeadLinks(filename):

	global liveFileDir, staticFileDir, mediaFileDir

	with open(filename,'r') as f:
		s = f.read()

	soup = BeautifulSoup(s)
	soup.prettify()

	for div in soup.find('div', { 'id' : 'mw-content-text' }).findAll('a'):

		hreflink = str(div['href'].encode('utf-8'))
		#print(hreflink)
		if (hreflink[:1] != '#' and '../' in hreflink) or 'redlink=1' in hreflink:
			#div['href'] = div['href'].replace('/wiki/','../en/')
			#div['href'] += '.html'
			print(hreflink)
			checkfile = hreflink.replace('..',staticFileDir+'/wiki')
			print(checkfile)
			if os.path.isfile(checkfile):
				print('Static: '+hreflink)
			else:
				#div['class']='sever'
				hreflink = 'http://en.wikipedia.org/'+hreflink.replace('../en','wiki')
				#del(div['href'])
				#print(div['class'])
				div.unwrap()
				#print('Unwraped: '+hreflink)

			#try:
				#print(div['href'])
			#except:
			#	pass

	soup.prettify()

	try:
		f = open(infile,'w')
		print(soup,file=f)
		f.close
	except:
		pass			


i=0
for infile in glob.glob( os.path.join(mediaFileDir, '*.html') ):
	i+=1
	print('Article #'+str(i))
	print(infile)
	removeDeadLinks(infile)