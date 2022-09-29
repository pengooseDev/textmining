from nltk.tokenize import WordPunctTokenizer

para = "Hello everyone. It's good to see you. Let's start our text mining class!"
print(WordPunctTokenizer().tokenize(para))
