# import nltk
# nltk.download('all')
# from nltk.stem import WordNetLemmatizer
# lemmatizer = WordNetLemmatizer()
import re
from MyNewestKazzo import word_count
with open("J. K. Rowling - Harry Potter 1 - Sorcerer's Stone.txt") as f:
    s = f.read()
egg = (word_count(s))
final_string = re.sub(r'[^\w\s]','',egg)
print(final_string)

# #
#
#
