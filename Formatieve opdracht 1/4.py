def palin(string):
    if string[::-1] == string:
        return True
    return False


print(palin("racecar"))