# 문제 링크: https://www.acmicpc.net/problem/14963

c = {i: 4 for i in range(2, 12)}
c[10] = 16
x = 21
n = int(input())
for _ in range(n):
    i = int(input())
    c[i] -= 1
    x -= i

print(['VUCI', 'DOSTA'][sum(c[i] for i in range(2, 12) if i > x) * 2 >= 52 - n])
