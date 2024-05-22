# 문제 링크: https://www.acmicpc.net/problem/7567

s = input()
print(sum(5 if i == j else 10 for i, j in zip(' ' + s, s)))
