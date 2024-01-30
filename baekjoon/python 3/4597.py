# 문제 링크: https://www.acmicpc.net/problem/4597

while (s := input().strip()) != '#':
    print(s.replace(s[-1], str((s.count('1') + (s[-1] == 'o')) % 2)))
