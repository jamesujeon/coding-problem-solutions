# 문제 링크: https://www.acmicpc.net/problem/11759

s, v1, v2 = map(int, input().split())

i = s // v1
while i >= 0 and (s - v1 * i) % v2 != 0:
    i -= 1

if i > -1:
    print(i, (s - v1 * i) // v2)
else:
    print("Impossible")
