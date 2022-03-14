# 문제 링크: https://www.acmicpc.net/problem/1075

N, F = int(input()), int(input())

result = (N - N % 100) % F
if result > 0:
    result = F - result

print(str(result).zfill(2))
