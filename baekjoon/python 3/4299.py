# 문제 링크: https://www.acmicpc.net/problem/4299

s, d = map(int, input().split())

a = (s + d) // 2
b = (s - d) // 2

if a + b == s and a - b == d and s >= d:
    print(a, b)
else:
    print(-1)
