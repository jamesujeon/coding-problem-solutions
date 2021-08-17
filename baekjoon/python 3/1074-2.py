# 문제 링크: https://www.acmicpc.net/problem/1074

N, r, c = map(int, input().split())


order = 0
while N:
    size = 2 ** (N - 1)
    quad = 0
    if r >= size:
        quad += 2
        r -= size
    if c >= size:
        quad += 1
        c -= size

    order += quad * size**2
    N -= 1


print(order)