# 문제 링크: https://www.acmicpc.net/problem/1718

s, e = input(), input()
print(''.join(chr((ord(s[i]) - ord(e[i % len(e)]) - 1) % 26 + 97) if s[i] != ' ' else ' ' for i in range(len(s))))
