import pandas as pd
from konlpy.tag import Okt  # konlpy에서 Twitter 형태소 분석기를 import

df = pd.read_csv('../data/daum_movie_review.csv')

twitter_tag = Okt()


def my_tokenizer(doc):
    return [token for token, pos in twitter_tag.pos(doc) if pos in ['Noun', 'Verb', 'Adjective']]


print("나만의 토크나이저 결과:", my_tokenizer(df.review[1]))
