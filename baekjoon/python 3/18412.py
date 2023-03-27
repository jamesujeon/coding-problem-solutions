# 문제 링크: https://www.acmicpc.net/problem/18412

_, A, B = map(int, input().split())
S = input()

print(S[:A - 1] + S[A - 1:B][::-1] + S[B:])
