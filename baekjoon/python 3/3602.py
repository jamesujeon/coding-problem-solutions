# 문제 링크: https://www.acmicpc.net/problem/3602

b, w = map(int, input().split())

print(int((min(b, w) * 2 + (b != w))**.5) if max(b, w) > 0 else 'Impossible')
