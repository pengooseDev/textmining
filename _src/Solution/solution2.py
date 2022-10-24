#0. SSL Err handler
import nltk
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

# (1) import movie_reviews
import nltk
nltk.download('movie_reviews')

# (2) useRegex and make tokenizer(len>=4)
from nltk.corpus import movie_reviews
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

tokenizer = RegexpTokenizer("[\w']{4,}")
# set stopWords
english_stops = set(stopwords.words('english'))
documents = [movie_reviews.raw(fileid) for fileid in movie_reviews.fileids()]
# use regexTokenizer and remove stopWords
tokens = [[token for token in tokenizer.tokenize(doc) if token not in english_stops] for doc in documents]

# (4)~(5) set docs in dictionary, make feature.
word_count = {}
for text in tokens:
    for word in text:
        word_count[word] = word_count.get(word, 0) + 1 # 빈도 계산

sorted_features = sorted(word_count, key=word_count.get, reverse=True)
# get top 20 features
word_features = sorted_features[:20]


from sklearn.feature_extraction.text import CountVectorizer
# create word_features
cv = CountVectorizer(vocabulary=word_features) # 리뷰 문서에 대해 fit_transform 적용
reviews_cv = cv.fit_transform(documents)

#(7) print all of the vetor.
print(reviews_cv.toarray())



