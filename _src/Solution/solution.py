#0. SSL Err handler (Mac환경에서 SSL 이슈가 있어 추가한 코드입니다.)
import nltk
import ssl
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

# (1) download "shakespeare-macbeth" and read it
nltk.download('gutenberg')
from nltk.corpus import gutenberg
file_names = gutenberg.fileids()
doc_macbeth = gutenberg.open('shakespeare-macbeth.txt').read()


# (2) create regexTokenizer (len>=4) and tokenize
from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer("[\w]{4,}")
tokens_macbeth = tokenizer.tokenize(doc_macbeth.lower())

# (3) remove stopwords("en")
from nltk.corpus import stopwords
english_stops = set(stopwords.words('english'))
result_macbeth = [word for word in tokens_macbeth if word not in english_stops]

# (4) create wordDictionary
macbeth_word_count = dict()
for word in result_macbeth:
    macbeth_word_count[word] = macbeth_word_count.get(word, 0) + 1

# (5) sort wordCount and show matplotlib bar
sorted_word_count = sorted(macbeth_word_count, key=macbeth_word_count.get, reverse=True)

import matplotlib.pyplot as plt
n = sorted_word_count[:15][::-1]
w = [macbeth_word_count[key] for key in n]
plt.barh(range(len(n)),w,tick_label=n)
plt.show()


# (6) draw wordCould
from wordcloud import WordCloud
wordcloud = WordCloud(max_font_size=60)
wordcloud.generate_from_frequencies(macbeth_word_count)
plt.axis("off")
plt.imshow(wordcloud)
plt.show()

