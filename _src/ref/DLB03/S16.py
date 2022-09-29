import nltk
from nltk.corpus import gutenberg
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords  # 일반적으로 분석대상이 아닌 단어들
from wordcloud import WordCloud
import matplotlib.pyplot as plt

doc_alice = gutenberg.open('carroll-alice.txt').read()
tokenizer = RegexpTokenizer("[\w']{3,}")
reg_tokens_alice = tokenizer.tokenize(doc_alice.lower())
english_stops = set(stopwords.words('english'))  # 반복이 되지 않도록 set으로 변환
result_alice = [word for word in reg_tokens_alice if word not in english_stops]  # stopwords를 제외한 단어들만으로 list를 생성

my_tag_set = ['NN', 'VB', 'VBD', 'JJ']
my_words = [word for word, tag in nltk.pos_tag(result_alice) if tag in my_tag_set]

alice_word_count = dict()
for word in my_words:
    alice_word_count[word] = alice_word_count.get(word, 0) + 1

wordcloud = WordCloud(max_font_size=60).generate_from_frequencies(alice_word_count)
plt.figure()
plt.axis("off")
plt.imshow(wordcloud, interpolation="bilinear")
plt.show()
