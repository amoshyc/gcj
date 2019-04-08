from math import gcd
from string import ascii_uppercase

TC = int(input())
for tc in range(1, TC + 1):
    N, L = map(int, input().split())
    A = list(map(int, input().split()))

    for pivot in range(len(A) - 1):
        if A[pivot] != A[pivot + 1]:
            break
    
    B = [-1 for _ in range(L + 1)]
    B[pivot + 1] = gcd(A[pivot], A[pivot + 1])

    for i in range(pivot, -1, -1):
        B[i] = A[i] // B[i + 1]
    for i in range(pivot + 2, L + 1):
        B[i] = A[i - 1] // B[i - 1]

    primes = sorted(list(set(B)))
    mapping = dict()
    for p, c in zip(primes, ascii_uppercase):
        mapping[p] = c

    ans = ''.join(mapping[b] for b in B)
    print('Case #{}: {}'.format(tc, ans))

