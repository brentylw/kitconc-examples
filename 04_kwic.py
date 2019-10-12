# -*- coding: utf-8 -*-
"""
Kitconc examples
@author: jlopes@usp.br
"""
from kitconc.kit_corpus import Corpus 
corpus = Corpus('kitconc-examples/workspace','ads','english')
kwic = corpus.kwic('experience',show_progress=True)
kwic.sort('R1','R2','R3')
print(kwic.df.head(10))
kwic.save_excel(corpus.output_path + 'kwic.xlsx',highlight='R1 R2 R3')