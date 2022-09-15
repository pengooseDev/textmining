import nltk
import ssl
from nltk.corpus import gutenberg

## Set SSL Setting
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    print("err")
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

# Code

#nltk.download('gutenberg') # 다운로드
file_names = gutenberg.fileids() # 제공하는 파일명을 읽어와서 출력
print(file_names)



from nltk.tokenize import word_tokenize
nltk.download('punkt')
doc_alice = gutenberg.open('carroll-alice.txt').read()
print('Length of document:', len(doc_alice))
tokens_alice = word_tokenize(doc_alice) # word_tokenize()로 토큰화 실행
print('Num of tokens used:', len(tokens_alice))
