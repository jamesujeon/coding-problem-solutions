# 문제 링크: https://www.acmicpc.net/problem/28014

N = int(input())
H = list(map(int, input().split()))

print(sum(H[i - 1] <= H[i] for i in range(1, N)) + 1)
