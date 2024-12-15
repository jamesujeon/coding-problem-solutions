# 문제 링크: https://www.acmicpc.net/problem/15181

while (s := input()) != '#':
    s = list(map(ord, s))
    b = all((b - a) % 7 in (2, 4, 6) for a, b in zip(s, s[1:]))

    print(['Ouch! That hurts my ears.', 'That music is beautiful.'][b])
