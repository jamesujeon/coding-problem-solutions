# 문제 링크: https://www.acmicpc.net/problem/2997

a, b, c = sorted(map(int, input().split()))

if b - a == c - b:
    print(c * 2 - b)
elif b - a > c - b:
    print((a + b) // 2)
else:
    print((b + c) // 2)
