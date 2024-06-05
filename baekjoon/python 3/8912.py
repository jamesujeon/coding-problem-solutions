# 문제 링크: https://www.acmicpc.net/problem/8912

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    print(sum(sum(a[j] <= a[i] for j in range(i)) for i in range(1, n)))
