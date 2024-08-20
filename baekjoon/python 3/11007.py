# 문제 링크: https://www.acmicpc.net/problem/11007

for _ in range(int(input())):
    input()

    s = ''
    c = list(map(chr, range(97, 123)))
    for a in map(int, input().split()):
        s += c[a]
        c = [c.pop(a)] + c

    print(s)
