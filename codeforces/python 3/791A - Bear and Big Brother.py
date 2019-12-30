# 문제 링크: http://codeforces.com/problemset/problem/791/A

a, b = map(int, input().split())

years = 0
while a <= b:
  a *= 3
  b *= 2
  years += 1

print(years)