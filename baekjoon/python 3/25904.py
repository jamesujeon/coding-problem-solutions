# 문제 링크: https://www.acmicpc.net/problem/25904

N, X = map(int, input().split())
T = list(map(int, input().split()))

i = 0
while T[i] >= X:
    X += 1
    i = (i + 1) % N

print(i + 1)
