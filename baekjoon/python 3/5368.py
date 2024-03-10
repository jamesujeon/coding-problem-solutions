# 문제 링크: https://www.acmicpc.net/problem/5368

for _ in range(int(input())):
    s, p = (), []
    for i in range(int(input())):
        for j, c in enumerate(input()):
            if c == 's':
                s = (i, j)
            elif c == 'p':
                p.append((i, j))

    d = min((((s[0] - px)**2 + (s[1] - py)**2)**.5, px, py) for px, py in p)

    print(f'({s[0]},{s[1]}):({d[1]},{d[2]}):{d[0]:.2f}')
