from __future__ import print_function
import urllib2, urllib
from bs4 import BeautifulSoup, Comment
import time
import os

liveFileDir = '/wiki/liveArticles/'  # dir of your live Wikipedia articles downloaded from scrapeWikiVital.py
staticFileDir = '/VOLUMES/LIBRARYBOX/static-Wikipedia-100/wiki'  # dir of where you want the static copies of the Wikipedia articles
#mediaFileDir = staticFileDir+'/wiki/en'  # the static articles will be placed within a /wiki/en/ for the English versions


def downloadMedia(line):
	global liveFileDir, staticFileDir, mediaFileDir
	

	mediaFile = urllib.unquote(line).decode('utf8').strip()
	url = 'http:'+mediaFile
	mediaFile = mediaFile.replace('//upload.wikimedia.org/wikipedia','').strip()
	mediaFile = mediaFile.replace('//upload.wikimedia.org','').strip()
	mediaFile = mediaFile.encode('utf-8')
	url = url.encode('utf-8')


	mediaFileDir = staticFileDir+os.path.dirname(mediaFile)
	print('Dirname: '+os.path.dirname(mediaFile))
	print('mediaFile= '+mediaFile)
	#print(mediaFileDir)

	print('URL: '+url)
	print('Save As: '+staticFileDir+mediaFile)
	print('Create Folder: '+mediaFileDir)


	if not os.path.exists(mediaFileDir):
		try:
			os.makedirs(mediaFileDir)
		except:
			pass

	try:
		s = urllib2.urlopen(url).read()
		f = open(staticFileDir+mediaFile,'w')
		print(s,file=f)
		f.close
		print('File Downloaded')
		#time.sleep(0.5)  # to be nice to Wikipedia's servers
	except:
		print('Error retrieving file: '+url)
		print(staticFileDir+mediaFile)
		f = open('lists/getVitalImg-ErrorLog.txt','w')
		print(url,file=f)
		f.close





with open('lists/listInfoBoxImgs-nodup.txt','r') as f:
	i=0
	for line in f:
		i+=1

		print('Media #'+str(i))
		mediaFile = urllib.unquote(line).decode('utf8').strip()
		url = 'http:'+mediaFile
		mediaFile = mediaFile.replace('//upload.wikimedia.org/wikipedia','').strip()
		mediaFile = mediaFile.replace('//upload.wikimedia.org','').strip()
		mediaFile = mediaFile.encode('utf-8')
		url = url.encode('utf-8')

		print('Check File Exist?: '+staticFileDir+mediaFile)
		if os.path.isfile(staticFileDir+mediaFile):
			print(mediaFile+' already downloaded')  # in case the script gets interrupted, we don't want to re-download already acquired files
		else:
			time.sleep(0.3)
			downloadMedia(line)