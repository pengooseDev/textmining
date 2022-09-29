# 토크나이즈 - stemming || regex || "lammatize" - 불용어처리 - 품사태깅.
# - 품사태깅엔 렘마타이즈가 유리함.

# 워드 클라우드 복습.
import nltk
from nltk.corpus import gutenberg

doc_hamlet = gutenberg.open('shakespeare-hamlet.txt').read()

from nltk.tokenize import word_tokenize
tokens_hamlet = word_tokenize(doc_hamlet)

# lancStemmer : https://excelsior-cjh.tistory.com/67
from nltk.stem.lancaster import LancasterStemmer
lanc_stemmer = LancasterStemmer()
lanc_tokens_hamlet = [lanc_stemmer.stem(i) for i in tokens_hamlet]

print(lanc_tokens_hamlet[:20])
#from nltk.stem import WordNetLemmatizer
#lemmatizer = WordNetLemmatizer()

# lemmatizer은 Class이며 lemmatize라는 메서드를 제공한다.
# 해당 메서드는 사전적 정의와 비슷하게 바꿔줌.
#lem_tokens_hamlet = [lemmatizer.lemmatize(i) for i in tokens_hamlet]

