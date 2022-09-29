from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

para = "Hello everyone. It's good to see you. Let's start our text mining class!"
tokens = word_tokenize(para)  # 토큰화 실행
print(tokens)

stemmer = PorterStemmer()
result = [stemmer.stem(token) for token in tokens]  # 모든 토큰에 대해 스테밍 실행
print(result)
