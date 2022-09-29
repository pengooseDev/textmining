from nltk.corpus import gutenberg

file_names = gutenberg.fileids()  # 파일 제목을 읽어온다.
print(file_names)

doc_alice = gutenberg.open('carroll-alice.txt').read()
print('#Num of characters used:', len(doc_alice))  # 사용된 문자의 수
print('#Text sample:')
print(doc_alice[:500])  # 앞의 500자만 출력
