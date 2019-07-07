L, R = map(int, input().split())

if R >= L + 2019:
    print('0')
else:
    xs = [x % 2019 for x in range(L, R + 1)]
    vs = []
    for i in range(len(xs)):
        for j in range(i + 1, len(xs)):
            vs.append((xs[i] * xs[j]) % 2019)
    print(min(vs))