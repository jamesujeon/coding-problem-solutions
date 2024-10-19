# 문제 링크: https://www.acmicpc.net/problem/13774

while (s := input()) != '#':
    for i in range(len(s)):
        p = s[:i] + s[i + 1:]
        if p == p[::-1]:
            print(p)
            break
    else:
        print('not possible')
