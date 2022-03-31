# 문제 링크: https://www.acmicpc.net/problem/2506

input()
scores = input().split('0')

print(sum(s.count('1') * (s.count('1') + 1) // 2 for s in scores))
