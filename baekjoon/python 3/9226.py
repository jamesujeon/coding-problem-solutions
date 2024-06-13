# 문제 링크: https://www.acmicpc.net/problem/9226

while (s := input()) != '#':
    i = 0
    while i < len(s) and s[i] not in "aeiou":
        i += 1

    print(s[i:] + s[:i] + "ay")
