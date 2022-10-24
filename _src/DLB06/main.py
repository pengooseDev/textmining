import nltk
import ssl

#다운로드

#try:
#    _create_unverified_https_context = ssl._create_unverified_context
#except AttributeError:
#    pass
#else:
#    ssl._create_default_https_context = _create_unverified_https_context
#
#nltk.download('movie_reviews')


from nltk.corpus import movie_reviews
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords # 일반적으로 분석대상이 아닌 단어들
tokenizer = RegexpTokenizer("[\w']{3,}") # 정규표현식으로 토크나이저를 정의
english_stops = set(stopwords.words('english')) # 영어 불용어를 가져옴
# movie_reviews의 함수 중 fields()와 raw()를 이용해 전체 문서를 가져옴
documents = [movie_reviews.raw(fileid) for fileid in movie_reviews.fileids()]
# 토큰화와 불용어 처리를 동시에 실행
tokens = [[token for token in tokenizer.tokenize(doc) if token not in english_stops] for doc in documents]


word_count = {} # 단어 빈도 계산을 위한 딕셔너리
for text in tokens: # 각 문서 별로 토큰화한 결과에 대해
    for word in text: # 문서 별 토큰의 각 단어에 대해
        word_count[word] = word_count.get(word, 0) + 1 # 빈도 계산

sorted_features = sorted(word_count, key=word_count.get, reverse=True)
word_features = sorted_features[:1000] # 상위 1,000개 단어로 특성 집합 생성
print(word_features[:10]) # 특성 집합의 상위 10개 단어 확인

def document_features(document, word_features):
    word_count = {}
    for word in document: # document에 있는 단어들에 대해 빈도수를 먼저 계산
        word_count[word] = word_count.get(word, 0) + 1
        features = []
    # word_features의 단어에 대해 계산된 빈도수를 feature에 추가
    for word in word_features:
        features.append(word_count.get(word, 0)) # 빈도가 없는 단어는 0을 입력
        return features


# 앞서 작성한 함수로 문서들을 변환
feature_sets = [document_features(d, word_features) for d in tokens]
# 첫째 feature set의 내용을 앞 10개만 word_features의 단어와 함께 출력
for i in range(10):
    print(f'({word_features[i]}, {feature_sets[0][i]})', end=', ')
print()
print(feature_sets[0][-10:]) # feature set의 뒤 10개만 출력


