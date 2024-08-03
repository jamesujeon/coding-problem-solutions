# 문제 링크: https://www.acmicpc.net/problem/10643

S = [int(input()) for _ in range(8)] * 2

print(max(sum(S[i:i + 4]) for i in range(8)))
