RomanNumber = "VII"
Integer = 0
if "C" in RomanNumber:
    Integer += 100
if "IV" in RomanNumber:
    Integer += 4
elif "III" in RomanNumber:
    Integer += 3
elif "II" in RomanNumber:
    Integer += 2
elif "I" in RomanNumber:
    Integer += 1
elif "V" in RomanNumber:
    Integer += 5
print(Integer)