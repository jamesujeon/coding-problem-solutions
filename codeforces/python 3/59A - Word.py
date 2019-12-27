# 문제 링크: http://codeforces.com/problemset/problem/59/A

s = input()

print(s.lower() if sum(1 if ch.islower() else -1 for ch in s) >= 0 else s.upper())