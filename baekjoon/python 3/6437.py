# 문제 링크: https://www.acmicpc.net/problem/6437

import sys

def get_score(p, s):
    if s == 1:
        return 'Hole-in-one.'
    elif p == s:
        return 'Par.'
    elif p == s + 1:
        return 'Birdie.'
    elif p == s + 2:
        return 'Eagle.'
    elif p == s + 3:
        return 'Double eagle.'
    elif p == s - 1:
        return 'Bogey.'
    else:
        return 'Double Bogey.'

for i, input in enumerate(sys.stdin):
    p, s = map(int, input.split())
    if p == 0:
        break

    print(f'Hole #{i + 1}')
    print(get_score(p, s))
    print()
