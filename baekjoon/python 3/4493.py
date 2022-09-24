# 문제 링크: https://www.acmicpc.net/problem/4493

import sys
input = sys.stdin.readline

def f(s1, s2):
    if (s1 == 'R' and s2 == 'S') or (s1 == 'P' and s2 == 'R') or (s1 == 'S' and s2 == 'P'):
        return 1
    elif s1 != s2:
        return 2
    else:
        return 0

for _ in range(int(input())):
    counts = [0] * 3
    for _ in range(int(input())):
        p1, p2 = input().split()
        counts[f(p1, p2)] += 1

    if counts[1] != counts[2]:
        print(f'Player {1 if counts[1] > counts[2] else 2}')
    else:
        print('TIE')
