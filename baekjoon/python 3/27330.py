# 문제 링크: https://www.acmicpc.net/problem/27330

_, A = input(), map(int, input().split())
_, B = input(), set(map(int, input().split()))

score = 0
for a in A:
    score += a
    if score in B:
        score = 0

print(score)
