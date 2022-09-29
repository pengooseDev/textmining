from nltk.corpus import gutenberg
from wordcloud import WordCloud
import matplotlib.pyplot as plt

doc_alice = gutenberg.open('carroll-alice.txt').read()
wordcloud = WordCloud().generate(doc_alice)

plt.axis("off")
plt.imshow(wordcloud, interpolation='bilinear')  # 이미지를 출력
plt.show()
