# 문제 링크: https://www.acmicpc.net/problem/1463

n = int(input())

counts = {0: 0, 1: 0}
def get_count(i):
  if i in counts:
    return counts[i]
  counts[i] = min(get_count(i // 3) + i % 3, get_count(i // 2) + i % 2) + 1
  return counts[i]

print(get_count(n))