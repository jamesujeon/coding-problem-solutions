# 문제 링크: http://codeforces.com/problemset/problem/263/A

matrix = [list(map(int, input().split())) for _ in range(5)]

index = (0, 0)
for i in range(5):
  try:
    index = (i, matrix[i].index(1))
    break
  except ValueError:
    continue

result = abs(index[0] - 2) + abs(index[1] - 2)

print(result)