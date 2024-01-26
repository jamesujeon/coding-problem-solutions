# 문제 링크: https://www.acmicpc.net/problem/4436

while True:
    try:
        n = int(input())
    except:
        break

    s = set(map(str, range(10)))
    k = 1
    while s:
        s -= set(str(k * n))
        k += 1

    print(k - 1)
