# 문제 링크: https://www.acmicpc.net/problem/13458

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

print(N - sum(max(a - B, 0) // -C for a in A))
