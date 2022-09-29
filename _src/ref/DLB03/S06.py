from nltk.corpus import gutenberg
from nltk.tokenize import RegexpTokenizer

doc_alice = gutenberg.open('carroll-alice.txt').read()
tokenizer = RegexpTokenizer("[\w']{3,}")
reg_tokens_alice = tokenizer.tokenize(doc_alice.lower())

print('#Num of tokens with RegexpTokenizer:', len(reg_tokens_alice))
print('#Token sample:')
print(reg_tokens_alice[:20])
