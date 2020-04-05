# 문제 링크: https://www.acmicpc.net/problem/1065

def is_hn(n):
  n = list(map(int, str(n)))
  return all(n[i] - n[i - 1] == n[1] - n[0] for i in range(2, len(n)))

print(sum(is_hn(i + 1) for i in range(int(input()))))
