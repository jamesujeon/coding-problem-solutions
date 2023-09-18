# 문제 링크: https://www.acmicpc.net/problem/27106

P = 100 - int(input())

cents = []
for c in 25, 10, 5, 1:
    cents.append(P // c)
    P %= c

print(*cents)
