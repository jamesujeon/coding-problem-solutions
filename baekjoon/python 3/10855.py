# 문제 링크: https://www.acmicpc.net/problem/10855

_, a = input(), list(map(int, input().split()))
print('yes' if a == sorted(a) else 'no')
