# 문제 링크: https://www.acmicpc.net/problem/15025

l, r = map(int, input().split())

if l > 0 or r > 0:
    print(f'{"Even" if l == r else "Odd"} {max(l, r) * 2}')
else:
    print('Not a moose')
