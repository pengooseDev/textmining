from nltk.tokenize import RegexpTokenizer

tokenizer = RegexpTokenizer("[\w']+")  # regular expression(정규식)을 이용한 tokenizer
# 단어단위로 tokenize \w:문자나 숫자를 의미 즉 문자나 숫자 혹은 '가 반복되는 것을 찾아냄
print(tokenizer.tokenize("Sorry, I can't go there."))
# can't를 하나의 단어로 인식

tokenizer = RegexpTokenizer("[\w]+")
print(tokenizer.tokenize("Sorry, I can't go there."))

text1 = "Sorry, I can't go there."
tokenizer = RegexpTokenizer("[\w']{3,}")
print(tokenizer.tokenize(text1.lower()))
