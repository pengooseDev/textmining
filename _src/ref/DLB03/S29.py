from konlpy.corpus import kolaw
from konlpy.tag import Okt
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

const_doc = kolaw.open('constitution.txt').read()
t = Okt()
tokens_const = t.nouns(const_doc)  # 형태소 단위로 tokenize 후 명사만 추출
tokens_const = [token for token in tokens_const if len(token) > 1]

font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
# 맥인 경우에는 아래와 같이 font_name을 지정
# font_name = 'AppleGothic'
rc('font', family=font_name)

const_cnt = {}
for word in tokens_const:
    const_cnt[word] = const_cnt.get(word, 0) + 1

font_path = 'c:/Windows/Fonts/malgun.ttf'
# 맥인 경우에는 아래와 같이 font_path를 지정
# font_path = 'AppleGothic'
wordcloud = WordCloud(
    font_path=font_path,
    max_font_size=100,
    width=800,  # 이미지 너비 지정
    height=400,  # 이미지 높이 지정
    background_color='white',  # 이미지 배경색 지정
    max_words=50)
wordcloud.generate_from_frequencies(const_cnt)  # 원문이 아닌 형태소 분석 결과로부터 워드클라우드를 생성
wordcloud.to_file("const.png")  # 생성한 이미지를 파일로 저장

plt.axis("off")
plt.imshow(wordcloud, interpolation='bilinear')
plt.show()
