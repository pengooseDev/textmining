from nltk.corpus import movie_reviews
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords  # 일반적으로 분석대상이 아닌 단어들

# words() 대신 raw()를 이용해 원문을 가져옴
documents = [movie_reviews.raw(fileid) for fileid in movie_reviews.fileids()]

tokenizer = RegexpTokenizer("[\w']{3,}")  # 정규포현식으로 토크나이저를 정의
english_stops = set(stopwords.words('english'))  # 영어 불용어를 가져옴
# stopwords의 적용과 토큰화를 동시에 수행.
tokens = [[token for token in tokenizer.tokenize(doc) if token not in english_stops] for doc in documents]

word_count = {}
for text in tokens:
    for word in text:
        word_count[word] = word_count.get(word, 0) + 1
sorted_features = sorted(word_count, key=word_count.get, reverse=True)

word_features = sorted_features[:1000]  # 빈도가 높은 상위 1000개의 단어만 추출하여 features를 구성


def document_features(document, word_features):
    word_count = {}
    for word in document:  # document에 있는 단어들에 대해 빈도수를 먼저 계산
        word_count[word] = word_count.get(word, 0) + 1

    features = []
    for word in word_features:  # word_features의 단어에 대해 계산된 빈도수를 feature에 추가
        features.append(word_count.get(word, 0))  # 빈도가 없는 단어는 0을 입력
    return features


word_features_ex = ['one', 'two', 'teen', 'couples', 'solo']
doc_ex = ['two', 'two', 'couples']
print(document_features(doc_ex, word_features_ex))
