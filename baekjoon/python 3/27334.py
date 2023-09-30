# 문제 링크: https://www.acmicpc.net/problem/27334

N, A = int(input()), list(map(int, input().split()))

B = sorted(A)
for a in A:
    print(B.index(a) + 1)
