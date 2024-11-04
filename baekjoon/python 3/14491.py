# 문제 링크: https://www.acmicpc.net/problem/14491

t = int(input())
s = ''
while t > 0:
    s += str(t % 9)
    t //= 9

print(s[::-1])
