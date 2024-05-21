# 문제 링크: https://www.acmicpc.net/problem/6979

for _ in range(int(input())):
    n = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))

    d = max([j - i for i in range(n - 1) for j in range(i + 1, n) if X[i] <= Y[j]] + [0])
    print(f"The maximum distance is {d}\n")
