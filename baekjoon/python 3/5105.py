# 문제 링크: https://www.acmicpc.net/problem/5105

while (s := input()) != '#':
    S, *L = s.split()

    h = [int(S)]
    for d in L:
        n = h[-1] + int(d[1]) * (1 if d[0] == 'U' else -1)
        if n in h or n < 1 or n > 20:
            h = []
            break
        h.append(n)

    if not h:
        print("illegal")
    elif len(h) == 20:
        print("none")
    else:
        print(*sorted(set(range(1, 21)) - set(h)))
