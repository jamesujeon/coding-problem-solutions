# 문제 링크: https://www.acmicpc.net/problem/17284

money = 5000
for n in map(int, input().split()):
    money -= [500, 800, 1000][n - 1]

print(money)
