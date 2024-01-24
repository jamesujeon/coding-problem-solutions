# 문제 링크: https://www.acmicpc.net/problem/4327

import sys
input = sys.stdin.readline

while True:
    n1, n2, n3, n4 = map(int, input().split())
    if n1 == n2 == n3 == n4 == 0:
        break

    print((120 + (n1 - n2) % 40 + (n3 - n2) % 40 + (n3 - n4) % 40) * 9)
