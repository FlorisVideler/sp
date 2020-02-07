# Uit deze opdracht kwam ik niet dus heb ik deze code gebruikt: https://www.programiz.com/python-programming/examples/fibonacci-recursion
# Ook na de uitleg op de website snap ik nog steeds niet echt hoe deze werkt.


def fiboncci(n, a):
    if n <= 1:
        return n
    else:
        return fiboncci(n - 1, 1) + fiboncci(n - 2, 2)


print(fiboncci(6, 0))
