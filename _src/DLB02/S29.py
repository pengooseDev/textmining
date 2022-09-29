import nltk
from nltk.tokenize import word_tokenize

tokens = word_tokenize("Hello everyone. It's good to see you. Let's start our text mining class!")

my_tag_set = ['NN', 'VB', 'JJ']
my_words = [word for word, tag in nltk.pos_tag(tokens) if tag in my_tag_set]
print(my_words)

words_with_tag = ['/'.join(item) for item in nltk.pos_tag(tokens)]
print(words_with_tag)
