# 문제 링크: https://www.acmicpc.net/problem/9584

import sys
input = sys.stdin.readline

s = input().strip()
v = []
for _ in range(int(input())):
    c = input().strip()
    if all(s[i] == '*' or s[i] == c[i] for i in range(9)):
        v.append(c)

print(len(v))
print(*v, sep='\n')
