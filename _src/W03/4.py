from nltk.corpus import gutenberg
from nltk.tokenize import word_tokenize

print("========Tokenize=========")
# alice.txt 객체 선언
alice = gutenberg.open('carroll-alice.txt').read()
# Tokenize
tokens_alice = word_tokenize(alice) # word_tokenize()로 토큰화 실행

######################################################
print("========Nomarlization : Stem =========")
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
# 삼항 연산자 내부의 for문 실행. stemmer애 존재하는 어간 추출을 통한 정규화.
stemmer_token_alice = [stemmer.stem(i) for i in tokens_alice]

print("======== Nomarlization : WordnetLemmatizer =========")

from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
lem_tokens_alice = [lemmatizer.lemmatize(token) for token in tokens_alice]

print("======== Nomarlization : Regex =========")
from nltk.tokenize import RegexpTokenizer
# 세 문자 이상의 단어만 추출
tokenizer = RegexpTokenizer("[\w']{3,}")
# 소문자 변환 후 토큰화 실행
reg_tokens_alice = tokenizer.tokenize(alice.lower())

######################################################

#각각 정규화 한 Data들을 List에 넣어줌.
normalized_data = [stemmer_token_alice, lem_tokens_alice, reg_tokens_alice]
# map이 Object를 return해서 일단 pass

print("======== 불용어 제거 =========")
from nltk.corpus import stopwords
english_stops = set(stopwords.words('english'))


# 불용어처리 callBack 함수 (정규화 데이터)=> 불용어 처리 데이터
def return_stopwords(normalized_data):
    return [i for i in normalized_data if i not in english_stops]

# map을 사용해 normalizedData를 받아 불용어 처리가 끝난 data return.
# newIterable = map(callbackFunc, iterable)

result_alice = return_stopwords(reg_tokens_alice)


print("======== 단어 빈도별 계산 =========")
stemmer_alice_word_count = dict() #안씀
lem_alice_word_count = dict() #안씀
regex_alice_word_count = dict()

for word in result_alice: # 모든 토큰에 대해
    regex_alice_word_count[word] = regex_alice_word_count.get(word, 0) + 1
    sorted_word_count = sorted(regex_alice_word_count, key=regex_alice_word_count.get, \
reverse=True)

#print(regex_alice_word_count)


print("======== 빈도 순위 확인 =========")
for key in sorted_word_count[:20]: #빈도수 상위 20개의 단어를 출력
    print(f'{repr(key)}: {regex_alice_word_count[key]}', end=', ')

print("======== MatplotLib =========")
import matplotlib.pyplot as plt
# 빈도수 상위 20개의 단어를 추출해 역순으로 정렬
n = sorted_word_count[:20][::-1]
# 20개 단어에 대한 빈도
w = [regex_alice_word_count[key] for key in n]
# 수평 막대그래프
plt.barh(range(len(n)),w,tick_label=n)

# plt.show() # Window Rendering

# WordCount 실행 예제

from wordcloud import WordCloud
# 워드 클라우드 이미지 생성
wordcloud = WordCloud()
wordcloud.generate(alice)
plt.axis("off") # 축이 보이지 않게 설정
plt.imshow(wordcloud) #plt.imshow()로 이미지 출력
#plt.show()

import numpy as np
from PIL import Image
# 사용할 배경이미지를 불러와서 numpy array로 변환
alice_mask = np.array(Image.open("alice_mask.png"))
wc = WordCloud(background_color="white", # 배경색 지정
max_words=30, # 출력할 최대 단어 수
mask=alice_mask, # 배경으로 사용할 이미지
contour_width=3, # 테두리 굵기
contour_color='steelblue') # 테두리 색
wc.generate_from_frequencies(regex_alice_word_count) # 워드 클라우드 생성
wc.to_file("alice.png") # 필요한 경우 결과를 이미지 파일로 저장
plt.axis("off")
plt.imshow(wc)
plt.show()
