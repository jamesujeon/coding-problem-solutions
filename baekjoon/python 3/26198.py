# 문제 링크: https://www.acmicpc.net/problem/26198

import sys
input = sys.stdin.readline

values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

for _ in range(int(input())):
    s = input()
    print(sum(s.count(ch) * values[ch] for ch in "IVXLCDM"))
