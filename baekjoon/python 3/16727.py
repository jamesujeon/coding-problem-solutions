# 문제 링크: https://www.acmicpc.net/problem/16727

p1, s1 = map(int, input().split())
s2, p2 = map(int, input().split())

p, s = p1 + p2, s1 + s2
if p == s:
    p, s = p2, s1

if p > s:
    print('Persepolis')
elif p < s:
    print('Esteghlal')
else:
    print('Penalty')
