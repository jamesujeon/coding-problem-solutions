# 문제 링크: https://www.acmicpc.net/problem/18247

for _ in range(int(input())):
    N, M = map(int, input().split())

    if N > 11 and M > 3:
        print(M * 11 + 4)
    else:
        print(-1)
