import nltk
from nltk.corpus import gutenberg
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords  # 일반적으로 분석대상이 아닌 단어들

doc_alice = gutenberg.open('carroll-alice.txt').read()
tokenizer = RegexpTokenizer("[\w']{3,}")
reg_tokens_alice = tokenizer.tokenize(doc_alice.lower())
english_stops = set(stopwords.words('english'))  # 반복이 되지 않도록 set으로 변환
result_alice = [word for word in reg_tokens_alice if word not in english_stops]  # stopwords를 제외한 단어들만으로 list를 생성

my_tag_set = ['NN', 'VB', 'VBD', 'JJ']
my_words = [word for word, tag in nltk.pos_tag(result_alice) if tag in my_tag_set]
print(my_words)

alice_word_count = dict()
for word in my_words:
    alice_word_count[word] = alice_word_count.get(word, 0) + 1
print('#Num of used words:', len(alice_word_count))

sorted_word_count = sorted(alice_word_count, key=alice_word_count.get, reverse=True)
print("#Top 20 high frequency words:")
for key in sorted_word_count[:20]:  # 빈도수 상위 20개의 단어를 출력
    print(f'{repr(key)}: {alice_word_count[key]}', end=', ')
