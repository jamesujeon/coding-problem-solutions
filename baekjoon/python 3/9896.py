# 문제 링크: https://www.acmicpc.net/problem/9896

_, s = input(), input()
print(s[0] + ''.join(str(int(i) ^ int(j)) for i, j in zip(s, s[1:])))
