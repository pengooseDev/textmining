# 4. 품사 태깅 (POS-Tagging)

import nltk
from nltk.tokenize import word_tokenize
tokens = word_tokenize("Hello everyone. It's good to see you. Let's start our text mining class!")
print(nltk.pos_tag(tokens))


#원하는 품사의 단어만 추출할 수 있음.

my_tag_set = ['NN', 'VB', 'JJ']
my_words = [word for word, tag in nltk.pos_tag(tokens) if tag in my_tag_set]
print(my_words)



# JJ Adjective(형용사)
# NN Noun(명사)
# NNP Proper noun(고유명사)
# RB Adverb(부사)
# VB Verb(동사)
# PRP Pronoun(대명사)
# CC coordinating conjunction(접속사)
# IN preposition (전치사)
# UH Interjection(감탄사)