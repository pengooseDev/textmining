def document_features(document, word_features):
    word_count = {}
    for word in document:  # document에 있는 단어들에 대해 빈도수를 먼저 계산
        word_count[word] = word_count.get(word, 0) + 1
    print(word_count)

    features = []
    for word in word_features:  # word_features의 단어에 대해 계산된 빈도수를 feature에 추가
        features.append(word_count.get(word, 0))  # 빈도가 없는 단어는 0을 입력
    return features


doc_ex = ['two', 'two', 'couples']
word_features_ex = ['one', 'two', 'teen', 'couples', 'solo']
print(document_features(doc_ex, word_features_ex))
