# 문제 링크: https://www.acmicpc.net/problem/4841

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    s = input().strip()

    result = ''
    count = 1
    for i in range(1, len(s)):
        if s[i] != s[i - 1]:
            result += f'{count}{s[i - 1]}'
            count = 0
        count += 1
    result += f'{count}{s[-1]}'

    print(result)
