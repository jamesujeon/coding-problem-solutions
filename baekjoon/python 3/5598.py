# 문제 링크: https://www.acmicpc.net/problem/5598

print(''.join(chr((ord(ch) - 68) % 26 + 65) for ch in input()))
