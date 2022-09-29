from konlpy.corpus import kolaw
from konlpy.tag import Okt

const_doc = kolaw.open('constitution.txt').read()
t = Okt()
tokens_const = t.nouns(const_doc)  # 형태소 단위로 tokenize 후 명사만 추출

print('#토큰의 수:', len(tokens_const))
print('#앞 100개의 토큰')
print(tokens_const[:100])
