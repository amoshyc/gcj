from random import shuffle, seed

seed(999)

def valid(pos1, pos2):
    r1, c1 = pos1
    r2, c2 = pos2
    if r1 == r2 or c1 == c2:
        return False
    if r1 - c1 == r2 - c2 or r1 + c1 == r2 + c2:
        return False
    return True

def check(R, C):
    steps = [(r, c) for r in range(R) for c in range(C)]
    shuffle(steps)

    for i in range(1, R * C):
        # Find a valid step in steps[i:] with steps[i - 1]
        for j in range(i, len(steps)):
            if valid(steps[i - 1], steps[j]):
                break
        else:
            return []
        steps[i], steps[j] = steps[j], steps[i]
    
    return steps
    

TC = int(input())
for tc in range(1, TC + 1):
    R, C = map(int, input().split())
    for _ in range(1000):
        ans = check(R, C)
        if len(ans) > 0:
            print('Case #{}: POSSIBLE'.format(tc))
            print('\n'.join('{} {}'.format(r + 1, c + 1) for r, c in ans))
            break
    else:
        print('Case #{}: IMPOSSIBLE'.format(tc))
    
