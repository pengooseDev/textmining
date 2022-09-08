# 정규화
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
print(stemmer.stem('cooking'), stemmer.stem('cookery'),stemmer.stem('cookbooks')) 

# 원형 : cooking, cookery, cookbooks
# >>> cook cookeri cookbook
