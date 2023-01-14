with open("I like to play the kazoo.txt") as f:
    s = f.read().split()
d = {}
for x in s:
    if d.get(x):
        d[x] += 1
    else:
        d[x] = 1


print(d)