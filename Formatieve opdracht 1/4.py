def palin(str):
    if str[::-1] == str:
        return True
    return False


print(palin("racecar"))