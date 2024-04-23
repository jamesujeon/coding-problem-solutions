# 문제 링크: https://www.acmicpc.net/problem/6796

import sys
input = sys.stdin.readline

v = [0, 0]
while (s := input().strip()) != '7':
    s = s.split()
    i, j = int(s[0]), s[1] == 'B'
    if i == 1:
        v[j] = int(s[2])
    elif i == 2:
        print(v[j])
    elif i > 2:
        v[j] = eval(f"int({v[j]}{'+*-/'[i - 3]}{v[s[2] == 'B']})")
