# 문제 링크: https://www.acmicpc.net/problem/26714

n, s = int(input()), input()
m = n // 10
t = 'T' * m

print(sum(s[i:i + m] == t for i in range(0, n, m)))
