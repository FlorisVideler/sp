# Bubble sort
def bs(unsortedlist):
    i = 0
    while i + 1 < len(unsortedlist):
        if unsortedlist[i] > unsortedlist[i + 1]:
            unsortedlist[i], unsortedlist[i + 1] = unsortedlist[i + 1], unsortedlist[i]
            i = 0
        else:
            i += 1
    return unsortedlist


unsortedlist = [10, 7, 8, 9, 10, 1, 5]
print(bs(unsortedlist))
