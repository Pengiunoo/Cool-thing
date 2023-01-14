
import random
from tqdm import tqdm
import string
random.choice(string.ascii_letters)


def get_random_alphanumeric_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
    print("Random alphanumeric String is:", result_str)



def appleinput(message="Please input the length of the password (a positive integer)"):
    while (True):
        try:
            string = input(message)
            assert "." not in string
            passwordlength = int(string)
            assert passwordlength > 0
            break
        except:
            print("please input an positive integer")

    password = ""
    for i in tqdm(range(passwordlength)):
        dog = str(random.randint(0, 9))
        password += dog
    return password

def orangeinput(message="Please input the length of the password (a positive integer)"):
    while (True):
        try:
            string = input(message)
            assert "." not in string
            egg = int(string)
            assert egg > 0
            break
        except:
            print("please input an positive integer")
password=""
    for i in tqdm(range(egg)):
        dog = str(random.randint(0, 9))
        password += dog



x = input("If you would like a number password, type N, if you would like a character password, type C")
if x == "N":
    print(appleinput())
elif x == "C":
    print(orangeinput())

else:
    print("please type either N or C")
    x = input("If you would like a number password, type N, if you would like a character password, type C")
