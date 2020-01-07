# 문제 링크: https://www.acmicpc.net/problem/9095

ns = [int(input()) for _ in range(int(input()))]

counts = {1: 1, 2: 2, 3: 4}
def count(i):
  if i in counts:
    return counts[i]
  counts[i] = count(i - 1) + count(i - 2) + count(i - 3)
  return counts[i]

for n in ns:
  print(count(n))