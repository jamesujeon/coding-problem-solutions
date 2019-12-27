# 문제 링크: http://codeforces.com/problemset/problem/230/B

_ = input()
x = map(int, input().split())

limit = int(1000000000000 ** .5) + 1
table = [0] * 2 + [1] * limit
for i in range(2, limit):
  if table[i]:
    for j in range(i ** 2, limit, i):
      table[j] = 0

for num in x:
  sqrt = int(num ** .5)
  print("YES" if table[sqrt] and sqrt ** 2 == num else "NO")