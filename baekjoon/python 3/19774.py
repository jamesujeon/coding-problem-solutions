# 문제 링크: https://www.acmicpc.net/problem/19774

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())

    print("YES" if ((n // 100)**2 + (n % 100)**2) % 7 == 1 else "NO")
