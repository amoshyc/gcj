TC = int(input())
for tc in range(1, TC + 1):
    N = input()
    A = N.replace('4', '3')
    B = ''.join(['1' if c == '4' else '0' for c in N]).lstrip('0')
    print('Case #{}: {} {}'.format(tc, A, B))