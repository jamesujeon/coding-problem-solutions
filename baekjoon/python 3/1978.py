# 문제 링크: https://www.acmicpc.net/problem/1978

p = [0, 0] + [1] * 999
for i in range(2, len(p)):
  j = i**2
  if j > len(p) - 1:
    break
  if p[i]:
    while j <= len(p) - 1:
      p[j] = 0
      j += i

input()
print(sum(p[n] for n in list(map(int, input().split()))))