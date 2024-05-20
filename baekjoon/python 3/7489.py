# 문제 링크: https://www.acmicpc.net/problem/7489

for _ in range(int(input())):
    f = 1
    for i in range(2, int(input()) + 1):
        f *= i

    print(str(f).rstrip('0')[-1])
