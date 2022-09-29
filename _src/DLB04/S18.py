import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

df = pd.read_csv('../data/daum_movie_review.csv')

daum_cv = CountVectorizer(max_features=1000)
daum_DTM = daum_cv.fit_transform(df.review)  # review를 이용하여 count vector를 학습하고, 변환
print(daum_cv.get_feature_names_out()[:100])  # count vector에 사용된 feature 이름을 반환
