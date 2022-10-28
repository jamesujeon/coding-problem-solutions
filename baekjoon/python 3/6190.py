# 문제 링크: https://www.acmicpc.net/problem/6190

N = int(input())

score = 0
while N > 1:
    N = 3 * N + 1 if N % 2 else N // 2
    score += 1

print(score)
