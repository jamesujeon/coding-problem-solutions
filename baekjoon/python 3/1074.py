# 문제 링크: https://www.acmicpc.net/problem/1074

N, r, c = map(int, input().split())


def get_order(size, r, c):
    if size == 1:
        return 0

    size //= 2
    quad = 0
    if r >= size:
        quad += 2
        r -= size
    if c >= size:
        quad += 1
        c -= size

    return quad * size**2 + get_order(size, r, c)


print(get_order(2**N, r, c))