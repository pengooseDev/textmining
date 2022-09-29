import numpy as np
from nltk.corpus import movie_reviews
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords  # 일반적으로 분석대상이 아닌 단어들
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

reviews = [movie_reviews.raw(fileid) for fileid in movie_reviews.fileids()]

tokenizer = RegexpTokenizer("[\w']{3,}")  # 정규포현식으로 토크나이저를 정의
english_stops = set(stopwords.words('english'))  # 영어 불용어를 가져옴
# stopwords의 적용과 토큰화를 동시에 수행.
tokens = [[token for token in tokenizer.tokenize(doc) if token not in english_stops] for doc in reviews]

word_count = {}
for text in tokens:
    for word in text:
        word_count[word] = word_count.get(word, 0) + 1
sorted_features = sorted(word_count, key=word_count.get, reverse=True)
word_features = sorted_features[:1000]  # 빈도가 높은 상위 1000개의 단어만 추출하여 features를 구성

################################################################################

tf = TfidfVectorizer(vocabulary=word_features)
reviews_tf = tf.fit_transform(reviews)

start = len(reviews[0]) // 2  # 첫째 리뷰의 문자수를 확인하고 뒤 절반을 가져오기 위해 중심점을 찾음
source = reviews[0][-start:]  # 중심점으로부터 뒤 절반을 가져와서 비교할 문서를 생성
source_tf = tf.transform([source])  # 코사인 유사도는 카운트 벡터에 대해 계산하므로 벡터로 변환
# transform은 반드시 리스트나 행렬 형태의 입력을 요구하므로 리스트로 만들어서 입력

sim_result_tf = cosine_similarity(source_tf, reviews_tf)  # 변환된 count vector와 기존 값들과의 similarity 계산

print('#가장 유사한 리뷰의 인덱스:', np.argmax(sim_result_tf[0]))
