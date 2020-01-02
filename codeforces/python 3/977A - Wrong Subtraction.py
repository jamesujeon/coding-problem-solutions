# 문제 링크: http://codeforces.com/problemset/problem/977/A

n, k = map(int, input().split())

for _ in range(k):
  n = n // 10 if n % 10 == 0 else n - 1

print(n)