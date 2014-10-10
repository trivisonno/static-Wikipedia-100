from __future__ import print_function
import urllib2, urllib
from bs4 import BeautifulSoup, Comment
import os
import glob

liveFileDir = '/wiki/liveArticles/'  # dir of your live Wikipedia articles downloaded from scrapeWikiVital.py
staticFileDir = '/VOLUMES/LIBRARYBOX/static-Wikipedia-100'  # dir of where you want the static copies of the Wikipedia articles
mediaFileDir = staticFileDir+'/wiki/en/'  # the static articles will be placed within a /wiki/en/ for the English versions

if not os.path.exists(mediaFileDir):
		try:
			os.makedirs(mediaFileDir)
		except:
			pass

def convertWikiArticle(filename):
	global liveFileDir, staticFileDir, mediaFileDir
	frenchlink = ''

	with open(filename,'r') as f:
		s = f.read()

	articleName = filename
	articleName = urllib.unquote(articleName).decode('utf8').strip()
	articleName = articleName.replace('.'+liveFileDir,'').strip()
	print(articleName)

	soup = BeautifulSoup(s)

	for div in soup.findAll('table', { 'class' : 'navbox' }):
		div.extract()

	for div in soup.findAll('table', { 'class' : 'persondata' }):
		div.extract()

	for div in soup.findAll('div', { 'class' : 'noprint' }):
		div.extract()

	for div in soup.findAll('ul', { 'class' : 'noprint' }):
		div.extract()		

	#for div in soup.findAll('div', { 'class' : 'thumb' }):
	#	div.extract()		

	for div in soup.findAll('div', { 'class' : 'hatnote' }):
		div.extract()		

	for div in soup.findAll('div', { 'class' : 'after-portlet' }):
		div.extract()		

	for div in soup.findAll('div', { 'id' : 'mw-head' }):
		div.extract()		

	for div in soup.findAll('div', { 'id' : 'p-logo' }):
		div.extract()		

	for div in soup.findAll('div', { 'id' : 'catlinks' }):
		div.extract()		

	for div in soup.findAll('div', { 'id' : 'p-interaction' }):
		div.extract()		

	for div in soup.findAll('div', { 'id' : 'p-tb' }):
		div.extract()		

	for div in soup.findAll('div', { 'id' : 'siteNotice' }):
		div.extract()		

	for div in soup.findAll('div', { 'id' : 'jump-to-nav' }):
		div.extract()		

	for div in soup.findAll('div', { 'id' : 'p-coll-print_export' }):
		div.extract()		

	for div in soup.findAll('div', { 'id' : 'section_SpokenWikipedia' }):
		div.extract()		

	for div in soup.findAll('div', { 'class' : 'ns-0' }):
		div.extract()		

	for div in soup.findAll('div', { 'class' : 'topicon' }):
		div.extract()		

	for div in soup.findAll('ul', { 'id' : 'footer-places' }):
		div.extract()		

	for div in soup.findAll('link', { 'rel' : 'dns-prefetch' }):
		div.extract()		

	for div in soup.findAll('link', { 'rel' : 'stylesheet' }):
		div.extract()		

	#for div in soup.findAll('table', { 'class' : 'plainlinks' }):
	#	div.extract()		

	for div in soup.findAll('script'):
		div.extract()		

	for div in soup.findAll('style'):
		div.extract()	

	for div in soup.findAll('span', { 'class' : 'mw-editsection' }):
		div.extract()	

	comments = soup.findAll(text=lambda text:isinstance(text, Comment))
	[comment.extract() for comment in comments]

	styletag = soup.new_tag('link')
	styletag.attrs['rel'] = 'stylesheet'
	styletag.attrs['href'] = '../css/style.css'
	soup.head.append(styletag)

	for div in soup.findAll('a', { 'class' : 'external text'}):
		div['target'] = '_blank'

	for div in soup.findAll('a', { 'dir' : 'ltr'}):
		#div.unwrap()
		pass

	for div in soup.findAll('a', { 'lang' : 'fr' , 'hreflang' : 'fr'}):
		frenchlink = div['href']
		print('FrenchLink: '+frenchlink)  # get the French link for the article to download, and write it to a file to get later
		
		if frenchlink != '':
			with open("lists/listFrenchArticles2Download.txt", "a") as myfile:
				myfile.write('http:'+frenchlink+'\n')
		else:
			with open("lists/missingVitalFrenchArticles.txt", "a") as myfile:
				myfile.write(articleName+'\n')

	for div in soup.findAll('li', { 'id' : 'footer-info-copyright'}):
		div.clear()
		div.append('Text is available under the ')
		new_tag = soup.new_tag("a", href="Text_of_Creative_Commons_Attribution-ShareAlike_3.0_Unported_License.html")
		new_tag.string = 'Creative Commons Attribution-ShareAlike License'
		div.append(new_tag)
		div.append('; additional copyright terms may apply to images, audio and video.  Please see this article on wikipedia.org for copyright information.')

	# Clear and then rebuild the navigation sidebar; needs to be rewritten in reverse order
	for div in soup.findAll('div', { 'id' : 'p-navigation' }):
		div.clear()

		new_tag = soup.new_tag('h3')
		new_tag.string = 'Search Wikipedia'
		div.append(new_tag)
		div.h3['id']='p-navigation-label'


		new_tag = soup.new_tag('input')
		#new_tag.string = 'Search'
		div.append(new_tag)
		div.input['id']='searchInput'
		div.input['type']='search'
		div.input['name']='search'
		div.input['accesskey']='f'
		div.input['placeholder']='Search'
		div.input['style']='margin-left:10px;margin-bottom:10px;width:130px;'


		new_tag = soup.new_tag('h3')
		new_tag.string = 'Navigation'
		div.append(new_tag)
		div.h3['id']='p-navigation-label'

		new_tag = soup.new_tag('div', { 'class' : "body" })
		div.append(new_tag)
		div.div['class']='body'

		new_tag = soup.new_tag('ul')
		div.div.append(new_tag)

		new_tag = soup.new_tag('li')
		div.div.ul.append(new_tag)
		new_tag = soup.new_tag('a')
		new_tag.string = ('Mathematics')
		div.li.append(new_tag)
		div.li.a['href']='../en/Subject_Mathematics.html'  

		new_tag = soup.new_tag('li')
		div.li.insert_before(new_tag)
		new_tag = soup.new_tag('a')
		new_tag.string = ('Technology')
		div.li.append(new_tag)
		div.li.a['href']='../en/Subject_Technology.html'  

		new_tag = soup.new_tag('li')
		div.li.insert_before(new_tag)
		new_tag = soup.new_tag('a')
		new_tag.string = ('Physical sciences')
		div.li.append(new_tag)
		div.li.a['href']='../en/Subject_Physical_sciences.html'  

		new_tag = soup.new_tag('li')
		div.li.insert_before(new_tag)
		new_tag = soup.new_tag('a')
		new_tag.string = ('Biology and health sciences')
		div.li.append(new_tag)
		div.li.a['href']='../en/Subject_Biology_and_health_sciences.html'  

		new_tag = soup.new_tag('li')
		div.li.insert_before(new_tag)
		new_tag = soup.new_tag('a')
		new_tag.string = ('Society and social sciences')
		div.li.append(new_tag)
		div.li.a['href']='../en/Subject_Society_and_social_sciences.html'  

		new_tag = soup.new_tag('li')
		div.li.insert_before(new_tag)
		new_tag = soup.new_tag('a')
		new_tag.string = ('Everyday life')
		div.li.append(new_tag)
		div.li.a['href']='../en/Subject_Everyday_life.html' 

		new_tag = soup.new_tag('li')
		div.li.insert_before(new_tag)
		new_tag = soup.new_tag('a')
		new_tag.string = ('Philosophy and religion')
		div.li.append(new_tag)
		div.li.a['href']='../en/Subject_Philosophy_and_religion.html'

		new_tag = soup.new_tag('li')
		div.li.insert_before(new_tag)
		new_tag = soup.new_tag('a')
		new_tag.string = ('Arts')
		div.li.append(new_tag)
		div.li.a['href']='../en/Subject_Arts.html'  

		new_tag = soup.new_tag('li')
		div.li.insert_before(new_tag)
		new_tag = soup.new_tag('a')
		new_tag.string = ('Geography')
		div.li.append(new_tag)
		div.li.a['href']='../en/Subject_Geography.html'  

		new_tag = soup.new_tag('li')
		div.li.insert_before(new_tag)
		new_tag = soup.new_tag('a')
		new_tag.string = ('History')
		div.li.append(new_tag)
		div.li.a['href']='../en/Subject_History.html'  

		new_tag = soup.new_tag('li')
		div.li.insert_before(new_tag)
		new_tag = soup.new_tag('a')
		new_tag.string = ('People')
		div.li.append(new_tag)
		div.li.a['href']='../en/Subject_People.html'  

		new_tag = soup.new_tag('li')
		div.li.insert_before(new_tag)
		new_tag = soup.new_tag('a')
		new_tag.string = 'Main Page'
		div.li.append(new_tag)
		div.li.a['href']='../en/Main_Page.html'

	# Clear and then rebuild the language sidebar
	for div in soup.findAll('div', { 'id' : 'p-lang' }):
		div.clear()
		new_tag = soup.new_tag('h3')
		new_tag.string = 'Languages'
		div.append(new_tag)
		div.h3['id']='p-lang-label'
		new_tag = soup.new_tag('div', { 'class' : "body" })
		div.append(new_tag)
		div.div['class']='body'
		new_tag = soup.new_tag('ul')
		div.div.append(new_tag)



		new_tag = soup.new_tag('li')
		div.div.ul.append(new_tag)


		if frenchlink != '':
			new_tag = soup.new_tag('a')	
			div.li.append(new_tag)
			div.li.a['href']='../fr/'+articleName  # needs to be changed to whatever the French title is
			new_tag.string = (u'Fran\u00E7ais')
		else:
			new_tag = soup.new_tag('span')



		new_tag = soup.new_tag('li')
		div.li.insert_before(new_tag)
		new_tag = soup.new_tag('a')
		new_tag.string = 'English'
		div.li.append(new_tag)
		div.li.a['href']='../en/'+articleName+'.html'
		

	for div in soup.find('div', { 'id' : 'mw-content-text' }).findAll('a'):

		hreflink = str(div['href'].encode('utf-8'))
		if hreflink[:1] != '#' and '/wiki/' in hreflink:
			div['href'] = div['href'].replace('/wiki/','../en/')
			div['href'] += '.html'

	
	try:
		for div in soup.find('div', { 'id' : 'mw-content-text' }).findAll('img'):
			
			imglink = str(div['src'].encode('utf-8'))
			print(imglink)
			#imglink = imglink.replace('//upload.wikimedia.org/wikipedia/','../')
			#print(imglink)
			if not '?' in imglink:
				with open("lists/listInfoBoxImgs.txt", "a") as myfile:
					myfile.write(imglink+'\n')

	except:
		pass	

	try:
		for div in soup.find('div', { 'id' : 'mw-content-text' }).findAll('source'):
			
			ogglink = str(div['src'].encode('utf-8'))
			print(ogglink)
			#ogglink = ogglink.replace('//upload.wikimedia.org/wikipedia/','../')
			#print(imglink)

			with open("lists/listInfoBoxOggs.txt", "a") as myfile:
				myfile.write(ogglink+'\n')

	except:
		pass			


	


	soup.prettify()
	

	new_soup = str(soup)
	new_soup = new_soup.replace('//upload.wikimedia.org/wikipedia/','../')
	

	try:
		path = staticFileDir  # I ran out of space on my laptop, so I'm just going to throw all these files on a USB
		f = open(path+'/wiki/en/'+articleName,'w')
		print(new_soup,file=f)
		f.close
	except:
		print('Static save failed!!!')

i=0
for infile in glob.glob( os.path.join('./wiki/liveArticles/', '*.html') ):
	i+=1
	print('Article #'+str(i))
	print(infile)
	convertWikiArticle(infile)

