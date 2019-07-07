from math import sqrt

N, D = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
for i in range(N):
    for j in range(i + 1, N):
        dis = sqrt(float(sum([(X[i][c] - X[j][c])**2 for c in range(D)])))
        if float(int(dis)) == dis:
            cnt += 1

print(cnt)
        
