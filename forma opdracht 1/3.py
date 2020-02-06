def count(lst, x):
    cntr = 0
    for i in lst:
        if i == x:
            cntr += 1

    return cntr

def diff(lst):
    return max(lst) - min(lst)

def onesnzeros(lst):
    c0 = count(lst, 0)
    c1 = count(lst, 1)
    if c0 > 12:
        return False
    if c1 <= c0:
        return False
    return True

print(count([1,1, 4, 5, 6, 8, 8, 8, 9, 9, 9, 9, 9, 1, 2, 4, 23], 8))
print(diff([1, 5454546, 6, 758483, 3]))
print(onesnzeros([0,1,1, 0,0,0,0,0,0,0,0,0,0,0]))
