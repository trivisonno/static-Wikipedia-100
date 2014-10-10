==Static-Wikipedia-100==

The Static-Wikipedia-100 repo is an attempt to generate a static and fully-contained 100-article version of Wikipedia for offline and remote use.  These 98 articles contain nearly 2,000 images.

More info here: http://en.wikipedia.org/wiki/Wikipedia:Vital_articles/Level/2

===Steps to generate the static version===

1. Run getListEnWikiVital100.py to generate the ListEnWikiVital100.txt file, that includes the article links to the 100-vital Wikipedia articles.
2. Run scrapeWikiVital.py to download live versions of the Vital Wikipedia articles.  They are placed in wiki/liveArticles/ as .html files. 
3. Run convertWiki2Static.py to convert the live verisons to static versions.
4. Run removeDeadLinks.py to remove links to articles not within the static set.
5. Run remoevDuplicateLines.py to remove duplicate links to images so we only download the links once.
6. Run getVitalImg.py to download images used in the static pages.
7. Finished! You now have your own miniature Wikipedia. 98 Articles and their images take up about 47MB of space.