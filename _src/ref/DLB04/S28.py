from nltk.corpus import movie_reviews
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords  # 일반적으로 분석대상이 아닌 단어들
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

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

# 모든 매개변수에 디폴트 값을 사용하는 경우
# cv = CountVectorizer()
# 앞에서 생성한 word_features를 이용하여 특성 집합을 지정하는 경우
cv = CountVectorizer(vocabulary=word_features)
# 특성 집합을 지정하지 않고 최대 특성의 수를 지정하는 경우
# cv = CountVectorizer(max_features=1000)
reviews_cv = cv.fit_transform(reviews)  # reviews를 이용하여 count vector를 학습하고, 변환

transformer = TfidfTransformer()
reviews_tfidf = transformer.fit_transform(reviews_cv)
print('#shape of tfidf matrix:', reviews_tfidf.shape)  # TF-IDF 행렬의 모양과 카운트 행렬의 모양이 일치하는 것을 확인

# 첫 리뷰의 카운트 벡터 중 앞 20개 값 출력
print('#20 count score of the first review:', reviews_cv[0].toarray()[0][:20])
# 첫 리뷰의 TF-IDF 벡터 중 앞 20개 값 출력
print('#20 tfidf score of the first review:', reviews_tfidf[0].toarray()[0][:20])
