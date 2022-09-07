# 문제 링크: https://www.acmicpc.net/problem/2953

scores = [sum(map(int, input().split())) for _ in range(5)]
max_score = max(scores)

print(scores.index(max_score) + 1, max_score)
