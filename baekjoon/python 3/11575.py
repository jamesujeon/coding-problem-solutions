# 문제 링크: https://www.acmicpc.net/problem/11575

for _ in range(int(input())):
    a, b = map(int, input().split())
    s = list(map(chr, ((a * i + b) % 26 + 65 for i in range(26))))

    print(''.join(s[ord(i) - 65] for i in input()))
