# 문제 링크: https://www.acmicpc.net/problem/24296

N = int(input())

while N % 2:
    N = N // 2 + 1

print(N)
