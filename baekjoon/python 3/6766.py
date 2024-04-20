# 문제 링크: https://www.acmicpc.net/problem/6766

K = int(input())

print(''.join(chr((ord(c) - 65 - 3 * (i + 1) - K) % 26 + 65) for i, c in enumerate(input())))
