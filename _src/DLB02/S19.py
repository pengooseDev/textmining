from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords  # 일반적으로 분석대상이 아닌 단어들

text1 = "Sorry, I couldn't go to movie yesterday."
tokenizer = RegexpTokenizer("[\w']+")
tokens = tokenizer.tokenize(text1.lower())  # word_tokenize로 토큰화

english_stops = set(stopwords.words('english'))  # 반복이 되지 않도록 set으로 변환
print(english_stops)

result = [word for word in tokens if word not in english_stops]  # stopwords를 제외한 단어들만으로 list를 생성
print(result)

my_stopword = ['i', 'go', 'to']  # 나만의 stopword를 리스트로 정의
result = [word for word in tokens if word not in my_stopword]
print(result)
