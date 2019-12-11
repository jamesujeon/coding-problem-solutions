# 문제 링크: http://codeforces.com/problemset/problem/266/B

n, t = map(int, input().split())
s = input()

for _ in range(t):
  s = s.replace('BG', 'GB')

print(s)