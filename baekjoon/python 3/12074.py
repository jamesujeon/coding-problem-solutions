# 문제 링크: https://www.acmicpc.net/problem/12074

s = '0'
for i in range(16):
    s += '0' + ''.join('10'[int(j)] for j in s[::-1])
s = s[:10**5]

for x in range(1, int(input()) + 1):
    print(f"Case #{x}: {s[int(input()) - 1]}")
