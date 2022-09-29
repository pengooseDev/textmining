from nltk.corpus import movie_reviews

print('#review count:', len(movie_reviews.fileids()))  # 영화 리뷰 문서의 id를 반환
print('#samples of file ids:', movie_reviews.fileids()[:10])  # id를 10개까지만 출력
print('#categories of reviews:', movie_reviews.categories())  # label, 즉 긍정인지 부정인지에 대한 분류
print('#num of "neg" reviews:', len(movie_reviews.fileids(categories='neg')))  # label이 부정인 문서들의 id를 반환
print('#num of "pos" reviews:', len(movie_reviews.fileids(categories='pos')))  # label이 긍정인 문서들의 id를 반환
fileid = movie_reviews.fileids()[0]  # 첫번째 문서의 id를 반환
print('#id of the first review:', fileid)
print('#first review content:\n', movie_reviews.raw(fileid)[:200])  # 첫번째 문서의 내용을 200자까지만 출력
print()
print('#sentence tokenization result:', movie_reviews.sents(fileid)[:2])  # 첫번째 문서를 sentence tokenize한 결과 중 앞 두 문장
print('#word tokenization result:', movie_reviews.words(fileid)[:20])  # 첫번째 문서를 word tokenize한 결과 중 앞 스무 단어
