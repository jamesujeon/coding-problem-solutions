# 문제 링크: https://www.acmicpc.net/problem/15874

k, _ = map(int, input().split())
s = list(input())

for i in range(len(s)):
    if s[i].isalpha():
        j = 65 if s[i].isupper() else 97
        s[i] = chr((ord(s[i]) - j + k) % 26 + j)

print(''.join(s))
