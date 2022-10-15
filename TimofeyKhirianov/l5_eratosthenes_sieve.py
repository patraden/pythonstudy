def sieve(n):
    """ Решето Эратосфена для числа n."""
    pass
    a = [True] * n  # все числа до N простые
    a[0] = a[1] = False
    for k in range(2, n):
        if a[k]:
            for m in range(2 * k, n, k):
                a[m] = False
    for k in range(n):
        print(k, "-", "простое" if a[k] else "составное")  # тернарный оператор в принте с if


sieve(100)
