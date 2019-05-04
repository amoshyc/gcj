import sys
from itertools import permutations
from collections import Counter, defaultdict

TC, F = map(int, input().split())

for tc in range(1, TC + 1):
    P = [''.join(p) for p in permutations('ABCDE')]

    # first char
    cnt = Counter()
    I0 = defaultdict(list)
    for i in range(119):
        print(5 * i + 1, flush=True)
        c = input()
        I0[c].append(5 * i + 1)
        cnt[c] += 1
    r0, _ = cnt.most_common()[-1]
    P = [p for p in P if p[0] == r0]

    # second char
    cnt = Counter()
    I1 = defaultdict(list)
    for i in range(23):
        print(I0[r0][i] + 1, flush=True)
        c = input()
        I1[c].append(I0[r0][i] + 1)
        cnt[c] += 1
    r1, _ = cnt.most_common()[-1]
    P = [p for p in P if p[1] == r1]

    # third char
    cnt = Counter()
    I2 = defaultdict(list)
    for i in range(5):
        print(I1[r1][i] + 1, flush=True)
        c = input()
        I2[c].append(I1[r1][i] + 1)
        cnt[c] += 1
    r2, _ = cnt.most_common()[-1]
    P = [p for p in P if p[2] == r2]

    print(I2[r2][0] + 1, flush=True)
    c = input()
    ans = P[0] if P[0][-2] != c else P[1]

    print(''.join(ans), flush=True)
    ok = input()

    
