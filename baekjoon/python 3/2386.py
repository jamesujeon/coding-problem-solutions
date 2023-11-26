# 문제 링크: https://www.acmicpc.net/problem/2386

while (s := input().lower()) != '#':
    print(s[0], s[2:].count(s[0]))
