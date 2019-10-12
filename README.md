
Kitconc
===========

Kitconc is a package for Corpus Linguistics and text analysis with Python. 
It contains, among other things, tools for creating:

* Corpora
* Frequency wordlists
* Keywords
* Concordance lines
* Collocates 
* N-gram lists
* Dispersion plots
* Excel data files 

The package is built on top of platforms and packages for scientific research: NLTK, pandas, XlsxWrite and sckit-learn. 
All in Anaconda Platform.

Requirements
=========

Kitconc requires a Python 3.6 (or later) installation along with:

* nltk
* pandas
* XlsxWrite
* matplotlib

It is suggested that users install Anaconda Platform as an easy option. 

Installation with pip
=========
(Make sure you have Python 3.6 (or later) and the required packages.)

Use the following command:
```bash
pip install kitconc
```

Installation from GitHub
=========
(Make sure you have Python 3.6 (or later) and the required packages.)

1. Download Kitconc from GitHub;
2. Extract its contents;
3. Open a terminal and navigate to the 'kitconc-master' folder;
4. Use the following command:
```bash
python setup.py install
```

Language resources
=========

Kitconc comes with some language resources for portuguese and english corpora.
It also has functions for adding your own language resources.

Usage example
=========

See how easy it is to use Kitconc:

(<a href='https://github.com/ilexistools/kitconc-examples'>Download examples...</a>)

Dowloading examples
-------------
```python
from kitconc.core import Examples 

Examples().download()
```

Adding a corpus
-------------
```python
from kitconc.kit_corpus import Corpus 
# reference to the corpus
corpus = Corpus('kitconc-examples/workspace','ads','english')
# add texts from source folder
corpus.add_texts('kitconc-examples/ads',show_progress=True)
```

Creating a wordlist 
-------------
```python
from kitconc.kit_corpus import Corpus 
# reference to the corpus
corpus = Corpus('kitconc-examples/workspace','ads','english')
# make wordlist
wordlist = corpus.wordlist(show_progress=True)
# print the top 10 
print(wordlist.df.head(10))
# save Excel file
wordlist.save_excel(corpus.output_path + 'wordlist.xlsx') 
```
<a href='https://raw.githubusercontent.com/ilexistools/kitconc-examples/master/images/wordlist.png'>See results...</a>

Extracting keywords 
-------------
```python
from kitconc.kit_corpus import Corpus 
corpus = Corpus('kitconc-examples/workspace','ads','english')
wordlist = corpus.wordlist(show_progress=True)
keywords = corpus.keywords(wordlist,show_progress=True)
print(keywords.df.head(10))
keywords.save_excel(corpus.output_path + 'keywords.xlsx')
```
<a href='https://raw.githubusercontent.com/ilexistools/kitconc-examples/master/images/keywords.png'>See results...</a>

Creating concordance lines 
-------------
```python
from kitconc.kit_corpus import Corpus

# reference to corpus 
corpus = Corpus('workspace','job_ads')

# make concordance lines 
kwic = corpus.kwic('experience')

# print 10 lines of concordances
print(kwic.df.head(10))

# save as Excel
kwic.save_excel(corpus.output_path + 'kwic_experience.xlsx')
```
<a href='https://raw.githubusercontent.com/ilexistools/kitconc-examples/master/images/concordance.png'>See results...</a>

Finding collocates 
-------------
```python
from kitconc.kit_corpus import Corpus

# reference to corpus 
corpus = Corpus('workspace','job_ads')

# make wordlist 
wordlist = corpus.wordlist()

# find collocates (t-score is the default measure)
collocates = corpus.collocates(wordlist, 'experience',coll_pos='NN JJ', left_span = 3, right_span=3)

#for mutual information, use:
#collocates = corpus.collocates(wordlist, 'experience',coll_pos='NN JJ', left_span = 3, right_span=3,
#measure=corpus.MUTUAL_INFORMATION)

# print the top 25 collocates
print(collocates.df.head(25))

# save as Excel
collocates.save_excel(corpus.output_path + 'collocates_experience.xlsx')
```
<a href='https://raw.githubusercontent.com/ilexistools/kitconc-examples/master/images/collocates.png'>See results...</a>

Making clusters 
-------------
```python
from kitconc.kit_corpus import Corpus

# reference to corpus 
corpus = Corpus('workspace','job_ads')

# make clusters
clusters = corpus.clusters('experience', size=3, min_freq = 3,min_range=2)

# print the top 25 clusters
print(clusters.df.head(25))

# save as Excel
clusters.save_xls(corpus.output_path + 'clusters_experience.xlsx')
```
<a href='https://raw.githubusercontent.com/ilexistools/kitconc-examples/master/images/clusters.png'>See results...</a>

Creating dispersion plots 
-------------
```python
from kitconc.kit_corpus import Corpus

# reference to corpus 
corpus = Corpus('workspace','job_ads')

# make dispersion plots
dispersion = corpus.dispersion('experience')

# print some data
print(dispersion.df.head(25))

# save as Excel
dispersion.save_excel(corpus.output_path + 'dispersion_experience.xlsx')
```
<a href='https://raw.githubusercontent.com/ilexistools/kitconc-examples/master/images/dispersion.png'>See results...</a>

Creating keywords dispersion plots 
-------------
```python
from kitconc.kit_corpus import Corpus

# reference to corpus 
corpus = Corpus('workspace','job_ads')

# make wordlist
wordlist = corpus.wordlist()

# make keywords 
keywords = corpus.keywords(wordlist)
wordlist = None

# make dispersion plots
dispersion = corpus.keywords_dispersion(keywords)

# print some data
print(dispersion.df.head(25))

# save as Excel
dispersion.save_excel(corpus.output_path + 'dispersion_keywords.xlsx')
```
<a href='https://raw.githubusercontent.com/ilexistools/kitconc-examples/master/images/dispersion_keywords.png'>See results...</a>


