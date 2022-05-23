# 문제 링크: https://www.acmicpc.net/problem/15474

n, a, b, c, d = map(int, input().split())

print(min(-(-n // a) * b, -(-n // c) * d))
