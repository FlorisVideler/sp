# De palindroom met soort van ingebouwde functie
def palin(string):
    if string[::-1] == string:
        return True
    return False


# Palindroom met zelfbedachte oplossing
def custom_palin(string):
    revstring = ""
    for i in range(len(string) - 1, -1, -1):
        revstring += string[i]
    if revstring == string:
        return True
    return False


print(palin("racecar"))
print(custom_palin("racecar"))
