# 문제 링크: https://www.acmicpc.net/problem/11816

X = input()

b = 10
if X[0] == '0':
    b = 16 if X[1] == 'x' else 8

print(int(X, b))
