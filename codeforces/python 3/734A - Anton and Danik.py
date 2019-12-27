# 문제 링크: http://codeforces.com/problemset/problem/734/A

_, s = input(), input()

bias = sum(1 if ch == 'A' else -1 for ch in s)

print("Anton" if bias > 0 else "Danik" if bias < 0 else "Friendship")