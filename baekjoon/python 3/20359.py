# 문제 링크: https://www.acmicpc.net/problem/20359

o = int(input())
p = 0
while o % 2 == 0:
    o //= 2
    p += 1

print(o, p)
