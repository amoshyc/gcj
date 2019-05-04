def win(a, b):
    if a == 'P' and b == 'R':
        return True
    if a == 'S' and b == 'P':
        return True
    if a == 'R' and b == 'S':
        return True
    return False


def solve(C):
    R = []
    for i in range(501):
        # win all
        for s in 'PSR':
            if all(win(s, c[i]) for c in C):
                return ''.join(R) + s

        # even for all
        for s in 'PSR':
            if all((not win(c[i], s)) for c in C):
                R.append(s)
                C = [c for c in C if not win(s, c[i])]
                break
        else:
            return 'IMPOSSIBLE'
    
    return 'IMPOSSIBLE'


TC = int(input())

for tc in range(1, TC + 1):
    A = int(input())
    C = [input() for _ in range(A)]
    for i, line in enumerate(C):
        C[i] = line * (1000 // len(line))
        C[i] = C[i][:500]

    print('Case #{}: {}'.format(tc, solve(C)))