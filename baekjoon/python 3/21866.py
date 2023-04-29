# 문제 링크: https://www.acmicpc.net/problem/21866

scores = list(map(int, input().split()))
max_scores = [100, 100, 200, 200, 300, 300, 400, 400, 500]

for i in range(9):
    if scores[i] > max_scores[i]:
        print("hacker")
        break
else:
    print("draw" if sum(scores) >= 100 else "none")
