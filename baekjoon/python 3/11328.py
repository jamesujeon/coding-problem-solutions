# 문제 링크: https://www.acmicpc.net/problem/11328

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a, b = input().split()
    print('Possible' if all(a.count(i) == b.count(i) for i in set(a)) else 'Impossible')
