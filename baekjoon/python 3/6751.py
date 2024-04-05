# 문제 링크: https://www.acmicpc.net/problem/6751

Y = int(input()) + 1
while len(set(str(Y))) < len(str(Y)):
    Y += 1

print(Y)
