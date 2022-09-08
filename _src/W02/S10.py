from nltk.tokenize import RegexpTokenizer
# RegexpTokenizer Class인듯?

text1 = "Sorry, I can't go there."
# 문자, 숫자, 언더바(_), 아포스트로피(＇)로 이루어진 `3자 이상의 단어`로 토크나이즈
# [\w']{3,} : 세 글자 이상만 return해줘.
tokenizer1 = RegexpTokenizer("[\w']{3,}")
print(tokenizer1.tokenize(text1.lower())) # 반드시 소문자로 바꾸고 정규식 적용

tokenizer2 = RegexpTokenizer("[\w']+")
print(tokenizer2.tokenize(text1.lower()))

#>>> ['sorry', "can't", 'there']