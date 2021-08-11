# 문제 링크: https://www.acmicpc.net/problem/15829

L = int(input())
S = input()


result = sum((ord(S[i]) - 96) * (31**i) for i in range(L)) % 1234567891


print(result)