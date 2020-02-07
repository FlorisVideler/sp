def avg(lst):
    # The easy way:
    # return sum(lst) / len(lst)

    # The hard way:
    lstsum = 0
    lstlen = 0
    for i in lst:
        lstsum += i
        lstlen += 1
    return lstsum / lstlen


print(avg([1, 2, 3, 4]))
