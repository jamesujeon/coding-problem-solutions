# 문제 링크: https://www.acmicpc.net/problem/8760

for _ in range(int(input())):
    W, K = map(int, input().split())

    print(W * K // 2)
