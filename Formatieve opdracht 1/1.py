#Mijn eigen oplossingen met 1 while loop

def pir(aantal):
    i = 1
    back = False
    while aantal >= i > 0:
        print("*" * i)
        if i == aantal:
            back = True
        if back:
            i -= 1
        else:
            i += 1


def pirrev(aantal):
    i = 1
    back = False
    while aantal >= i > 0:
        needed = aantal - i
        print(" "*needed + "*" * i)
        if i == aantal:
            back = True
        if back:
            i -= 1
        else:
            i += 1


# 2 for loops
def twofors(aantal):
    for i in range(1, aantal):
        print("*" * i)
    for i in range(aantal, 0, -1):
        print("*" * i)

def twoforsrev(aantal):
    for i in range(1, aantal):
        print(" " * (aantal-i) + "*" * i)
    for i in range(aantal, 0, -1):
        print(" " * (aantal-i) + "*" * i)


# 2 while loops
def twowhiles(aantal):
    i = 1
    while i <= aantal-1:
        print("*" * i)
        i += 1
    while i > 0:
        print("*" * i)
        i -= 1

def twowhilesrev(aantal):
    i = 1
    while i <= aantal - 1:
        print(" " * (aantal-i) + "*" * i)
        i += 1
    while i > 0:
        print(" " * (aantal-i) + "*" * i)
        i -= 1



# pir(int(input("Hoe groot?")))
# pirrev(int(input("Hoe groot?")))

twowhilesrev(5)



