import nltk
from numpy import savetxt

# nltk.download('all')
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
d = {}
with open("J. K. Rowling - Harry Potter 1 - Sorcerer's Stone.txt") as f:
   s = f.read()
kazo = s.split()
for word in kazo:
   word = lemmatizer.lemmatize(word)
   print(word)
   try:
       d[word] += 1
   except:
       d[word] = 1
savetxt(d,'cake.txt')
