# 문제 링크: https://www.acmicpc.net/problem/11772

X = 0
for _ in range(int(input())):
    P = input()
    X += int(P[:-1])**int(P[-1])

print(X)
