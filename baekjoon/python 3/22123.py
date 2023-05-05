# 문제 링크: https://www.acmicpc.net/problem/22123

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    S, F, k = input().split()
    s1, s2, s3 = map(int, S.split(':'))
    f1, f2, f3 = map(int, F.split(':'))

    s = s1 * 3600 + s2 * 60 + s3
    f = f1 * 3600 + f2 * 60 + f3
    if s >= f:
        f += 24 * 3600
    s += int(k) * 60

    if s <= f:
        print("Perfect")
    elif s <= f + 3600:
        print("Test")
    else:
        print("Fail")
