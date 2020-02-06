import string


def caesar(inp, rot):
    abclow = list(string.ascii_lowercase)
    abcup = list(string.ascii_uppercase)
    strlst = list(inp)
    for i in range(0, len(strlst)):
        try:
            abcindex = abclow.index(strlst[i].lower())
            if strlst[i].isupper():
                abcindex = int(str(abcindex) + "0")
        except ValueError:
            abcindex = strlst[i]
        strlst[i] = abcindex
    abcrotlow = abclow[rot:]
    abcrotlow.extend(abclow[:rot])
    abcrotup = abcup[rot:]
    abcrotup.extend(abcup[:rot])
    rotstr = ""
    for i in range(0, len(strlst)):
        if isinstance(strlst[i], int):
            if len(str(strlst[i])) > 2 and str(strlst[i])[-1] == "0":
                strlst[i] = int(str(strlst[i])[:-1])
                rotstr += abcrotup[strlst[i]]
            else:
                rotstr += abcrotlow[strlst[i]]
        else:
            rotstr += strlst[i]
    return rotstr


print(caesar(input("Geef een string: "), int(input("Geef een rotatie:"))))
