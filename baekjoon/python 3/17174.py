# 문제 링크: https://www.acmicpc.net/problem/17174

N, M = map(int, input().split())

count = 0
while N:
    count += N
    N //= M

print(count)
