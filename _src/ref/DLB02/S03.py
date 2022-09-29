from nltk.tokenize import sent_tokenize

para = "Hello everyone. It's good to see you. Let's start our text mining class!"
print(sent_tokenize(para))  # 주어진 text를 sentence 단위로 tokenize함. 주로 . ! ? 등을 이용
