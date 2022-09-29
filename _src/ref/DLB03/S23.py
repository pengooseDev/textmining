from konlpy.corpus import kolaw
from konlpy.tag import Okt
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


def word_graph(cnt, max_words=10):
    sorted_w = sorted(cnt.items(), key=lambda kv: kv[1])
    print(sorted_w[-max_words:])
    n, w = zip(*sorted_w[-max_words:])
    plt.barh(range(len(n)), w, tick_label=n)
    plt.savefig('bar.png')  # 필요한 경우, 그래프를 이미지 파일로 저장한다.
    plt.show()


word_graph(const_cnt, max_words=20)
