# 문제 링크: https://www.acmicpc.net/problem/15130

s = list(map(int, input().split()))
n = [(i, s[i]) for i in range(len(s)) if s[i] != 0]
c = (n[1][1] - n[0][1]) / (n[1][0] - n[0][0])

if c % 1 == 0:
    s[0] = n[0][1] - n[0][0] * int(c)
    for i in range(1, len(s)):
        s[i] = s[i - 1] + int(c)
    print(*s)
else:
    print(-1)
