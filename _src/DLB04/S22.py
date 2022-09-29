import pandas as pd
from konlpy.tag import Okt  # konlpy에서 Twitter 형태소 분석기를 import
from sklearn.feature_extraction.text import CountVectorizer

df = pd.read_csv('../data/daum_movie_review.csv')

twitter_tag = Okt()


def my_tokenizer(doc):
    return [token for token, pos in twitter_tag.pos(doc) if pos in ['Noun', 'Verb', 'Adjective']]


# 토크나이저와 특성의 최대개수를 지정
daum_cv = CountVectorizer(max_features=1000, tokenizer=my_tokenizer)
# 명사만 추출하고 싶은 경우에는 tokenizer에 'twitter_tag.nouns'를 바로 지정해도 됨
daum_DTM = daum_cv.fit_transform(df.review)  # review를 이용하여 count vector를 학습하고, 변환

print(repr(daum_DTM))
print(110800 / (14725 * 1000))

for word, count in zip(daum_cv.get_feature_names_out(), daum_DTM[1].toarray()[0]):
    if count > 0:
        print(word, ':', count, end=', ')
