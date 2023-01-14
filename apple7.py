s = "albertalwaysateapplesanywaysaaaa"
d = {}
for x in s:
    if d.get(x):
        d[x] += 1
    else:
        d[x] = 1


print(d)