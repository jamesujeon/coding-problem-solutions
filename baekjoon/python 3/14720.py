# 문제 링크: https://www.acmicpc.net/problem/14720

i = 0
input()
for j in map(int, input().split()):
    i += i % 3 == j

print(i)
