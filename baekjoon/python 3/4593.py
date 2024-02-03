# 문제 링크: https://www.acmicpc.net/problem/4593

while (s1 := input()) != 'E' and (s2 := input()) != 'E':
    c1 = c2 = 0
    for p1, p2 in zip(s1, s2):
        if p1 == p2:
            continue
        if (p1 == 'R' and p2 == 'S') or (p1 == 'P' and p2 == 'R') or (p1 == 'S' and p2 == 'P'):
            c1 += 1
        else:
            c2 += 1

    print(f'P1: {c1}')
    print(f'P2: {c2}')
