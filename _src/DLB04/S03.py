from nltk.corpus import movie_reviews

documents = [list(movie_reviews.words(fileid)) for fileid in movie_reviews.fileids()]
print(documents[0][:50])  # 첫째 문서의 앞 50개 단어를 출력

word_count = {}
for text in documents:
    for word in text:
        word_count[word] = word_count.get(word, 0) + 1

sorted_features = sorted(word_count, key=word_count.get, reverse=True)
for word in sorted_features[:10]:
    print(f"count of '{word}': {word_count[word]}", end=', ')
print()

for word in sorted_features[:10]:
    print(word, ':', word_count[word], end=', ')
print()
