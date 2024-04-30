# 문제 링크: https://www.acmicpc.net/problem/6860

a, b = input(), input()
g = []
for i in range(0, 10, 2):
    s = set(a[i:i + 2]).intersection(set(b[i:i + 2]))
    if any(j.isupper() for j in a[i:i + 2]) or any(j.isupper() for j in b[i:i + 2]):
        s.add(a[i].upper())
    g.append(s)

for _ in range(int(input())):
    c = input()
    print('Possible baby.' if all(c[i] in g[i] for i in range(5)) else 'Not their baby!')
