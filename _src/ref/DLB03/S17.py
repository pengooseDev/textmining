import numpy as np
import nltk
from nltk.corpus import gutenberg
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords  # 일반적으로 분석대상이 아닌 단어들
from wordcloud import WordCloud
from PIL import Image
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

alice_mask = np.array(Image.open("alice_mask.png"))  # 배경이미지를 불러와서 numpy array로 변환
wc = WordCloud(background_color="white",  # 배경색 지정
               max_words=30,  # 출력할 최대 단어 수
               mask=alice_mask,  # 배경으로 사용할 이미지
               contour_width=3,  # 테두리선의 크기
               contour_color='steelblue')  # 테두리선의 색
wc.generate_from_frequencies(alice_word_count)  # 워드 클라우드 생성
wc.to_file("alice.png")  # 결과를 이미지 파일로 저장

# 화면에 결과를 출력
plt.figure()
plt.axis("off")
plt.imshow(wc, interpolation='bilinear')
plt.show()
