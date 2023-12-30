# 문제 링크: https://www.acmicpc.net/problem/4072

while True:
    s = input()
    if s == '#':
        break

    print(' '.join(w[::-1] for w in s.split()))
