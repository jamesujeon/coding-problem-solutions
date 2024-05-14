# 문제 링크: https://www.acmicpc.net/problem/7120

s = input()

print(''.join(a for a, b in zip(s, ' ' + s) if a != b))
