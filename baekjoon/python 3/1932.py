# 문제 링크: https://www.acmicpc.net/problem/1932

ints = [list(map(int, input().split())) for _ in range(int(input()))]

for i in range(1, len(ints)):
  for j in range(len(ints[i])):
    if j == 0:
      ints[i][j] += ints[i - 1][0]
    elif j == len(ints[i]) - 1:
      ints[i][j] += ints[i - 1][-1]
    else:
      ints[i][j] += max(ints[i - 1][j - 1], ints[i - 1][j])

print(max(ints[-1]))