# 문제 링크: https://www.acmicpc.net/problem/26941

N = int(input())

h = b = 1
while True:
    b += ((h + 1) * 2 - 1)**2
    if b > N:
        break
    h += 1

print(h)
