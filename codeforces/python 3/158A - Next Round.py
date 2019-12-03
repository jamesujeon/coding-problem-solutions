# 문제 링크: http://codeforces.com/problemset/problem/158/A

n, k = map(int, input().split())
scores = list(map(int, input().split()))

advancer_count = 0
for score in scores:
  if score is 0 or score < scores[k - 1]:
    break

  advancer_count += 1

print(advancer_count)