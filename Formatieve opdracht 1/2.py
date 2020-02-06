# Let op spaties
def checkStrings(s1, s2):
    if len(s1) == len(s2):
        shortest = len(s1)
    elif len(s1) > len(s2):
        shortest = len(s1)
    else:
        shortest = len(s2)

    for i in range(0, shortest):
        if s1[i] != s2[i]:
            return f"Zit een verschil op index {i}"
    return "Er is geen verschil  "


# Let op niet spaties
def checkStringsns(s1, s2):
    s1, s2 = s1.replace(" ", ""), s2.replace(" ", "")
    if len(s1) == len(s2):
        shortest = len(s1)
    elif len(s1) > len(s2):
        shortest = len(s1)
    else:
        shortest = len(s2)

    for i in range(0, shortest):
        if s1[i] != s2[i]:
            return f"Zit een verschil op index {i}"
    return "Er is geen verschil"


while True:
    print(checkStrings(input("Eerste string"), input("Tweede string")))
    print(checkStringsns(input("Eerste string"), input("Tweede string")))
