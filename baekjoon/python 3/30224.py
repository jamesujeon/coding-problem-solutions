# 문제 링크: https://www.acmicpc.net/problem/30224

n = input()

if '7' not in n:
    print(0 if int(n) % 7 else 1)
else:
    print(2 if int(n) % 7 else 3)
