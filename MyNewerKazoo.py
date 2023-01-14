def kazoo(message):
    while True:
        kazoo = input(message)
        try:
            int(kazoo)
            break
        except:
            pass
    kazooThatIsReversed = kazoo[::-1]
    #debug the following (line number 11)
    if kazooThatIsReversed == kazoo:
        print(True)
    else:
        print(False)
kazoo("egg")

