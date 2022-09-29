from nltk.corpus import gutenberg
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

doc_alice = gutenberg.open('carroll-alice.txt').read()
tokens_alice = word_tokenize(doc_alice)  # 토큰화 실행

lemmatizer = WordNetLemmatizer()
lem_tokens_alice = [lemmatizer.lemmatize(token) for token in tokens_alice]  # 모든 토큰에 대해 스테밍 실행

print('#Num of tokens after lemmatization:', len(lem_tokens_alice))
print('#Token sample:')
print(lem_tokens_alice[:20])
