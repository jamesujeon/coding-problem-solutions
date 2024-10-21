# 문제 링크: https://www.acmicpc.net/problem/13775

K = int(input())
t = ''
for c in input():
    if c.isalpha():
        t += chr((ord(c) - 97 + 26 - K) % 26 + 97)
        K = K + 1 if K < 25 else 1
    else:
        t += c

print(t)
