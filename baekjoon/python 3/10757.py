# 문제 링크: https://www.acmicpc.net/problem/10757

a, b = input().split()

max_len = max(len(a), len(b))
a = list(map(int, a.zfill(max_len + 1)[::-1]))
b = list(map(int, b.zfill(max_len + 1)[::-1]))

for i in range(max_len):
    a[i] += b[i]
    if a[i] > 9:
        a[i + 1] += 1
        a[i] -= 10
if a[-1] == 0:
    a.pop()

print(''.join(map(str, a))[::-1])