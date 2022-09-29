from nltk.corpus import gutenberg
from nltk.tokenize import word_tokenize

doc_alice = gutenberg.open('carroll-alice.txt').read()
tokens_alice = word_tokenize(doc_alice)  # 토큰화 실행
print('#Num of tokens used:', len(tokens_alice))
print('#Token sample:')
print(tokens_alice[:20])
