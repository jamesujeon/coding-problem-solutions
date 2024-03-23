# 문제 링크: https://www.acmicpc.net/problem/5778

import sys
input = sys.stdin.readline

while (s := input().strip()) != '0 0':
    T = list(map(int, input().split()))

    print(sum(T.count(t) > 1 for t in set(T)))
