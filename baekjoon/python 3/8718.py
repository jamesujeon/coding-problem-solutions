# 문제 링크: https://www.acmicpc.net/problem/8718

x, k = map(int, input().split())

ratio = 0
if k * 7 <= x:
    ratio = 7
elif k * 3.5 <= x:
    ratio = 3.5
elif k * 1.75 <= x:
    ratio = 1.75

print(int(k * ratio * 1000))
