numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
p = []
not_p = []
for i in range(2, numbers[14] + 1):
    k = 0
    for j in range(1, i + 1):
        if i % j == 0 and i != j and j != 1:
            k += 1
    if k == 0:
        primes = True
        p.append(i)
    if k != 0:
        not_primes = False
        not_p.append(i)
print('Primes:', p)
print('Not Primes:', not_p)