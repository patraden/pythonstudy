def sieve(n):
    """ Eratosthenes sieve for n."""
    pass
    a = [True] * n
    a[0] = a[1] = False
    for k in range(2, n):
        if a[k]:
            for m in range(2 * k, n, k):
                a[m] = False
    for k in range(n):
        print(k, "-", "simple" if a[k] else "complex")


if __name__ == "__main__":
    sieve(100)
