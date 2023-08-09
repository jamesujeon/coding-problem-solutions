# 문제 링크: https://www.acmicpc.net/problem/25870

s = {}
for ch in input():
    s[ch] = s.get(ch, 0) + 1
s = s.values()

if all(v % 2 for v in s):
    print(1)
elif any(v % 2 for v in s):
    print(2)
else:
    print(0)
