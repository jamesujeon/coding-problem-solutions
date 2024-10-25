# 문제 링크: https://www.acmicpc.net/problem/14043

a, b = input(), input()
print("NA"[all(a.count(i) >= b.count(i) for i in set(b) if i != '*')])
