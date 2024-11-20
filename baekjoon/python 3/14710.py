# 문제 링크: https://www.acmicpc.net/problem/14710

h, m = map(int, input().split())
print('XO'[(h % 30) * 12 == m])
