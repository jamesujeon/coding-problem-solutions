# 문제 링크: https://www.acmicpc.net/problem/6876

import sys
input = sys.stdin.readline

d = "22233344455566677778889999"

for _ in range(int(input())):
    s = input().strip().replace('-', '')[:10]
    s = ''.join(d[ord(c) - 65] if c.isalpha() else c for c in s)

    print(f"{s[:3]}-{s[3:6]}-{s[6:]}")
