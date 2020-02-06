def bs(lst):
    i = 0
    while i+1 < len(lst):
        if lst[i] > lst[i + 1]:
            lst[i], lst[i + 1] = lst[i + 1], lst[i]
            i = 0
        else:
            i += 1
    return lst


lst = [10, 7, 8, 9, 10, 1, 5]
print(bs(lst))