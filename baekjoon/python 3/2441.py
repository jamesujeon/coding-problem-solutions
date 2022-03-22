# 문제 링크: https://www.acmicpc.net/problem/2441

N = int(input())

for i in range(N):
    print(' ' * i + '*' * (N - i))
