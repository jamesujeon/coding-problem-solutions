# 문제 링크: https://www.acmicpc.net/problem/2704

import sys
input = sys.stdin.readline
join = ''.join

for _ in range(int(input())):
    h, m, s = (f"{int(i):06b}" for i in input().split(':'))
    print(join(map(join, zip(h, m, s))), join((h, m, s)))
