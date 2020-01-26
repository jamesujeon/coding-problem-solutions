# 문제 링크: https://www.acmicpc.net/problem/1026

input()
inputs = lambda: map(int, input().split())
a = sorted(inputs())
b = sorted(inputs(), reverse=True)

result = sum(i * j for i, j in zip(a, b))

print(result)
