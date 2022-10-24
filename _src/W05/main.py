# 토크나이즈 - stemming || "lammatize" - 불용어처리 - 품사태깅.
# - 품사태깅엔 렘마타이즈가 유리함.

# 워드 클라우드 복습.
import nltk
from nltk.corpus import gutenberg

doc_hamlet = gutenberg.open('shakespeare-hamlet.txt').read()

from nltk.tokenize import word_tokenize
tokens_hamlet = word_tokenize(doc_hamlet)

## lancStemmer : https://excelsior-cjh.tistory.com/67
#from nltk.stem.lancaster import LancasterStemmer
#lanc_stemmer = LancasterStemmer()
#lanc_tokens_hamlet = [lanc_stemmer.stem(i) for i in tokens_hamlet]

#print(lanc_tokens_hamlet[:20])
### Tokenize
####렘마타이즈 아니라 포터스태머나 정규표현식 쓰는 경우, 아래 코드 변경한한 뒤, 불용어처리 res_hamlet삼항연산자 데이터 바꿔주면 됨.
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

# lemmatizer은 Class이며 lemmatize라는 메서드를 제공한다.
# 해당 메서드는 사전적 정의와 비슷하게 바꿔줌.
lem_tokens_hamlet = [lemmatizer.lemmatize(i) for i in tokens_hamlet]


## 불용어 처리.
from nltk.corpus import stopwords #일반적으로 분석대상이 아닌 단어들
eng_stops = set(stopwords.words('english'))
res_hamlet = [i for i in lem_tokens_hamlet if i not in eng_stops]

# 품사태깅
my_tag_set = ['NN', 'VB', 'VBD', 'JJ']
my_words = [i for i, tag in nltk.pos_tag(res_hamlet) if tag in my_tag_set]

hamlet_word_count = dict()
for i in my_words:
    # key값 가져와서 value += 1
    # get(i, 0) i의 값이 null일 경우 0을 넣어주세요라는 의미.
    hamlet_word_count[i] = hamlet_word_count.get(i, 0)+1

#순서대로 sort하기. List를 return함.
sorted_word_count = sorted(hamlet_word_count, key=hamlet_word_count.get, reverse=True)

import matplotlib.pyplot as plt

# 정렬된 단어 리스트에 대해 빈도수를 가져와서 새로운 리스트 생성
n = sorted_word_count[:20][::-1] # 빈도수 상위 20개의 단어를 추출하여 역순으로 정렬
w = [hamlet_word_count[key] for key in n]

#수직 막대그래프 bar
#수평 막대그래프 barh
plt.barh(range(len(n)),w,tick_label=n)
#plt.show()

## WordCould
from wordcloud import WordCloud

# Generate a word cloud image
wordcloud = WordCloud().generate(doc_hamlet)

plt.axis("off")
plt.imshow(wordcloud, interpolation='bilinear') #이미지를 출력
plt.show()
