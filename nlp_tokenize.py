# -*- coding: utf-8 -*-
"""NLP tokenize.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1NQtIXacKEdFIS0dzOAez6QWdGb6N5h8o
"""

import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
text = 'Hello! How are you doing today? I hope you are having a goog day.'
tokens = word_tokenize(text)
print(tokens)