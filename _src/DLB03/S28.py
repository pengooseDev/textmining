from konlpy.corpus import kolaw
from wordcloud import WordCloud
import matplotlib.pyplot as plt

const_doc = kolaw.open('constitution.txt').read()

font_path = 'c:/Windows/Fonts/malgun.ttf'
# 맥인 경우에는 아래와 같이 font_path를 지정
# font_path = 'AppleGothic'
wordcloud = WordCloud(font_path=font_path).generate(const_doc)

plt.axis("off")
plt.imshow(wordcloud, interpolation='bilinear')
plt.show()
