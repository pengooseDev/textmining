from nltk.tokenize import word_tokenize
from nltk.tokenize import WordPunctTokenizer  
para = "Hello everyone. It's good to see you. Let's start our text mining class!"

## 단어 토큰화는 두 가지 함수가 있음.
print(word_tokenize(para)) 
print(WordPunctTokenizer().tokenize(para))

