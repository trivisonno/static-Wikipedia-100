==Static-Wikipedia-100==

The Static-Wikipedia-100 repo is an attempt to generate a static and fully-contained 100-article version of Wikipedia for offline and remote use.
More info here: http://en.wikipedia.org/wiki/Wikipedia:Vital_articles/Level/2

===Steps to generate the static version===

1. Run getListEnWikiVital100.py to generate the ListEnWikiVital100.txt file, that includes the article links to the 100-vital Wikipedia articles.
2. Run scrapeWikiVital.py to download live versions of the Vital Wikipedia articles.  They are placed in wiki/liveArticles/ as .html files. 