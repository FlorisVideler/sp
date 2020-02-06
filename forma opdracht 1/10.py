def fiboncci(n, a):
    print(a, n)
    if n <= 1:
        return n
    else:
        return fiboncci(n - 1, 1) + fiboncci(n - 2, 2)

print(fiboncci(6, 0))