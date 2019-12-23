# 문제 링크: http://codeforces.com/problemset/problem/230/B

_ = input()
x = map(int, input().split())

limit = 1000001
table = [1] * 2 + [0] * limit
for i in range(2, limit):
  if not table[i]:
    for j in range(i ** 2, limit, i):
      table[j] = 1

for num in x:
  sqrt = int(num ** .5)
  print("NO" if table[sqrt] or sqrt ** 2 != num else "YES")