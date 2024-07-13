# 문제 링크: https://www.acmicpc.net/problem/9947

import sys
input = sys.stdin.readline

while (s := input().strip()) != '# #':
    p1, p2 = s.split()
    s = [0, 0]
    for _ in range(int(input())):
        c1, c2 = input().split()
        s[c1 != c2] += 1

    print(p1, s[0], p2, s[1])
