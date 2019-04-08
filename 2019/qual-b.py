TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    S = input()
    A = ['E' if c == 'S' else 'S' for c in S]
    A = ''.join(A)
    print('Case #{}: {}'.format(tc, A))