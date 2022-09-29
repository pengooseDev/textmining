from nltk.corpus import gutenberg
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

doc_alice = gutenberg.open('carroll-alice.txt').read()
tokens_alice = word_tokenize(doc_alice)  # 토큰화 실행

stemmer = PorterStemmer()
stem_tokens_alice = [stemmer.stem(token) for token in tokens_alice]  # 모든 토큰에 대해 스테밍 실행

print('#Num of tokens after stemming:', len(stem_tokens_alice))
print('#Token sample:')
print(stem_tokens_alice[:20])
