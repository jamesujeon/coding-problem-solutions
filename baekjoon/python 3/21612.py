# 문제 링크: https://www.acmicpc.net/problem/21612

B = int(input())

print(5 * B - 400)
print(-1 if B > 100 else (0 if B == 100 else 1))
