def prime(x, y):
    # insert comment
    primes = [True] * (y + 1)
    # 0 and 1 are not prime
    primes[0], primes[1] = False, False

    # insert comment
    for i in range(2, int(y ** 0.5) + 1):
        if primes[i]:
            # insert comment
            for j in range(i * i, y + 1, i):
                primes[j] = False
        res = [i for i in range(x, y + 1) if primes[i]]
    return res

x, y = 2, 7
res = prime(x, y)
print(res if res else "No")
