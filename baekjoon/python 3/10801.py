# 문제 링크: https://www.acmicpc.net/problem/10801

s = sum((i < j) - (i > j) for i, j in zip(map(int, input().split()), map(int, input().split())))
print('DAB'[(s < 0) - (s > 0)])
