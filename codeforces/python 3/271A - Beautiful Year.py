# 문제 링크: http://codeforces.com/problemset/problem/271/A

y = int(input()) + 1

while len(set(str(y))) < 4:
  y += 1

print(y)