# 문제 링크: http://codeforces.com/problemset/problem/158/A

n, k = map(int, input().split())
scores = list(map(int, input().split()))

advancer_count = 0
for i, score in enumerate(scores):
  if score > 0 and score >= scores[k - 1]:
    advancer_count += 1

print(advancer_count)