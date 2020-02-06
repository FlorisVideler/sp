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


pir(int(input("Hoe groot?")))
pirrev(int(input("Hoe groot?")))





