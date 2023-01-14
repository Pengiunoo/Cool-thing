# AThree = 7
# ATwo = 3
# AOne = 0
# BThree = 6
# BTwo = 4
# BOne = 1
#
# BThreepoint = BThree*3
# BTwopoint = BTwo*2
# AThreepoint = AThree*3
# ATwoPoint = ATwo*2
# BPoints = BThreepoint+BTwopoint+BOne

# APoints = AThreepoint+ATwoPoint+AOne
# if BPoints > APoints:
#     print("B")
# if APoints > BPoints:
#     print("A")
# if APoints == BPoints:
#     print("T")
def smartinput(doggo):
    while True:
        userinput=input(doggo)
        try:
            return int(userinput)
        except:
            print("Please input a integer")
    if input <1:
        print("no integers under 1")
        smartinput(doggo)
    egginput = input(doggo)





def apple():
    AThree = smartinput("Input the number of Three pointers for team apple (Between 0-100)")
    ATwo = smartinput("Input the number of Two pointers for team apple (Between 0-100)")
    AOne = smartinput("Input the number of One points for team apple (Between 0-100)")
    BThree = smartinput("Input the number of Three pointers for team banana (Between 0-100)")
    BTwo =smartinput("Input the number of Two pointers for team banana (Between 0-100)")
    BOne = smartinput("Input the number of One pointers for team banana (Between 0-100)")
    BThreepoint = BThree * 3
    BTwopoint = BTwo * 2
    AThreepoint = AThree * 3
    ATwoPoint = ATwo * 2
    BPoints = BThreepoint + BTwopoint + BOne
    APoints = AThreepoint + ATwoPoint + AOne
    # if input <1:
    #     raise Exception("Sorry, no numbers below 1")
    # if input >100:
    #     raise Exception("Sorry, no numbers above 100")

    if BPoints > APoints:
        return("B")
    elif APoints > BPoints:
        return("A")  
    elif APoints == BPoints:
        return("T")

print (apple())


