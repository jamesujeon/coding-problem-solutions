# 문제 링크: https://www.acmicpc.net/problem/6930

x, m = int(input()), int(input())

for n in range(1, m):
    if (x * n) % m == 1:
        print(n)
        break
else:
    print("No such integer exists.")
