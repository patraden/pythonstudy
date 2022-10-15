def lcs(a, b):  # largest common subsequence
    f = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    sub = [[[]] * (len(b) + 1) for _ in range(len(a) + 1)]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                f[i][j] = f[i - 1][j - 1] + 1
                sub[i][j] = sub[i - 1][j - 1] + [a[i - 1]]
            elif f[i - 1][j] >= f[i][j - 1]:
                sub[i][j] = sub[i - 1][j]
                f[i][j] = f[i - 1][j]
            else:
                f[i][j] = f[i][j - 1]
                sub[i][j] = sub[i][j - 1]
    return f[-1][-1], sub[-1][-1]


a1 = [1, 1, 2, 4, 5, 6, 7, 8, 8, 6, 5, 4, 3, 3, 3, 3, 32]
b1 = [1, 2, 4, 5, 5, 6, 7, 7, 8, 8, 8, 8, 8, 8, 4, 5, 6, 3, 3, 32]
print(lcs(a1, b1))
