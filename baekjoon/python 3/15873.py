# 문제 링크: https://www.acmicpc.net/problem/15873

n = input()

i = 1 + (n[1] == '0')
a = int(n[:i])
b = int(n[i:])

print(a + b)
