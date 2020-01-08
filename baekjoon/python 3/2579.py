# 문제 링크: https://www.acmicpc.net/problem/2579

stair_count = int(input())
scores = [0] + [int(input()) for _ in range(stair_count)]

max_scores = {(0, False): 0}
max_scores[(1, False)] = max_scores[(1, True)] = scores[1]

def max_score(n, is_consecutive=False):
  key = (n, is_consecutive)
  if key in max_scores:
    return max_scores[key]

  max_scores[key] = scores[n] + (max_score(n - 2) if is_consecutive else max(max_score(n - 2), max_score(n - 1, True)))
  return max_scores[key]

print(max_score(stair_count))