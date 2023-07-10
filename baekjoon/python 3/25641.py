# 문제 링크: https://www.acmicpc.net/problem/25641

input()
s = input()

while s.count('s') != s.count('t'):
    s = s[1:]

print(s)
