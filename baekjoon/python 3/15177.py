# 문제 링크: https://www.acmicpc.net/problem/15177

s1 = s2 = 0
for i in input().upper():
    s1 += 'KANGAROO'.count(i)
    s2 += 'KIWIBIRD'.count(i)

print(['Feud continues', 'Kangaroos', 'Kiwis'][(s1 != s2) + (s1 < s2)])
