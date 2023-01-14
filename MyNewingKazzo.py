import nltk
nltk.download('all')
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
d = {}
with open("J. K. Rowling - Harry Potter 1 - Sorcerer's Stone.txt") as f:
    s = f.read()
kazo = s.split()
for word in kazo:
    WordNetLemmatizer(word)
    print(word)
    try:
        d[word] += 1
    except:
        d[word] = 1

