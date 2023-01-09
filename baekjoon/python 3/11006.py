# 문제 링크: https://www.acmicpc.net/problem/11006

for _ in range(int(input())):
    N, M = map(int, input().split())

    print(M * 2 - N, N - M)
