# comparison of lemmatizing and stemming
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

stemmer = PorterStemmer()
print('stemming result:', stemmer.stem('believes'))

lemmatizer = WordNetLemmatizer()
print('lemmatizing result:', lemmatizer.lemmatize('believes'))
print('lemmatizing result:', lemmatizer.lemmatize('believes', pos='v'))
