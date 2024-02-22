# 문제 링크: https://www.acmicpc.net/problem/7600

while (s := input()) != '#':
    print(len(set(i for i in s.lower() if i.isalpha())))
