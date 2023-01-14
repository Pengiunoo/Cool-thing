s = "albertalwaysateapplesanywaysaaaa"
d = {}
for x in s:
    try:
        d[x] += 1
    except:
        d[x] = 1


print(d)




