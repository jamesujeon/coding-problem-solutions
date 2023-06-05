# 문제 링크: https://www.acmicpc.net/problem/23972

K, N = map(int, input().split())

result = -1
if N > 1:
    result = (K * N) // (N - 1)
    if (K * N) % (N - 1):
        result += 1

print(result)
