from nltk.tokenize import sent_tokenize

para_kor = "안녕하세요, 여러분. 만나서 반갑습니다. 이제 텍스트마이닝 클래스를 시작해봅시다!"
print(sent_tokenize(para_kor))  # 한국어에 대해서도 sentence tokenizer는 잘 동작함
