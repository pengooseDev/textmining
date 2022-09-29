import pandas as pd
from konlpy.tag import Okt  # konlpy에서 Twitter 형태소 분석기를 import

df = pd.read_csv('../data/daum_movie_review.csv')

twitter_tag = Okt()
print('#전체 형태소 결과:', twitter_tag.morphs(df.review[1]))
print('#명사만 추출:', twitter_tag.nouns(df.review[1]))
print('#품사 태깅 결과', twitter_tag.pos(df.review[1]))
