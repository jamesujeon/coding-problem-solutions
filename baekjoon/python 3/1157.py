# 문제 링크: https://www.acmicpc.net/problem/1157

d = {}
for c in input().upper():
  d[c] = d[c] + 1 if c in d else 1
d = sorted(d.items(), key=lambda x: x[1], reverse=True)

print(d[0][0] if len(d) == 1 or d[0][1] != d[1][1] else '?')