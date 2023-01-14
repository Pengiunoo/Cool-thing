x = 19
result = 0
xstring = str(x)
for w in xstring:
    result += int(w) ** 2
ystring = str(result)
if result == 1:
    print(True)

while True:
    result = 0
    for z in ystring:
        result += int(z) ** 2
    if result == 1:
        print(True)
        break
    ystring = str(result)












