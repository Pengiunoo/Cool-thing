
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
d = {}
pie = PorterStemmer()
words = ['run','ran','running']
for x in words:
    print(pie.stem(x))

