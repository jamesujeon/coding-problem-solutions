# 문제 링크: https://www.acmicpc.net/problem/4613

while (s := input()) != '#':
    print(sum((i + 1) * (ord(s[i]) - 64) for i in range(len(s)) if s[i].isalpha()))
