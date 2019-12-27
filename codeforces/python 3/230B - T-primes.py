# 문제 링크: http://codeforces.com/problemset/problem/230/B

_ = input()
x = map(int, input().split())

limit = int(1000000000000 ** .5) + 1
primes = [False] * 2 + [True] * (limit - 2)
for i in range(2, limit):
  if primes[i]:
    for j in range(i ** 2, limit, i):
      primes[j] = False

for num in x:
  sqrt = int(num ** .5)
  print("YES" if primes[sqrt] and sqrt ** 2 == num else "NO")