# 문제 링크: https://www.acmicpc.net/problem/2145

while (i := input()) != '0':
    while len(i) > 1:
        i = str(sum(map(int, i)))

    print(i)
