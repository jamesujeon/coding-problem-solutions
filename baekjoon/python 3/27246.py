# 문제 링크: https://www.acmicpc.net/problem/27246

n = int(input())

l, r = 0, n
while l < r:
    i = (l + r + 1) // 2
    if i * (i + 1) * (2 * i + 1) // 6 <= n:
        l = i
    else:
        r = i - 1

print(l)
