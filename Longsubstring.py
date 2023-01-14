from collections import Counter
s = "egg"
d = dict(Counter(s))
ListPear = list(d.values())
def apple(s):
    d = dict(Counter(s))
    if sum(d.values()) == len(d):
        print(f"{s} is cool")