# 문제 링크: https://www.acmicpc.net/problem/6890

k, m = input(), [c for c in input() if c.isalpha()]

print(''.join(chr((ord(m[i]) + ord(k[i % len(k)])) % 26 + 65) for i in range(len(m))))
