# 문제 링크: https://www.acmicpc.net/problem/2775

for _ in range(int(input())):
  k, n = int(input()), int(input())

  s = [i for i in range(n + 1)]
  for i in range(k):
    for j in range(1, n + 1):
      s[j] = s[j] + s[j - 1]

  print(s[-1])