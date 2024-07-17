# 문제 링크: https://www.acmicpc.net/problem/9971

while (s := input()) != 'ENDOFINPUT':
    s, _ = input(), input()
    print(''.join(chr((ord(c) - 70) % 26 + 65) if c.isalpha() else c for c in s))
