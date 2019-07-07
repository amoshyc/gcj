N = int(input())
A = list(map(int, input().split()))

C = 0
for i in range(1, N):
    C = A[i - 1] * 2 - C
C = A[-1] * 2 - C

M = [-1 for _ in range(N)]
M[0] = C // 2
for i in range(1, N):
    M[i] = A[i - 1] * 2 - M[i - 1]

print(' '.join(map(str, M)))