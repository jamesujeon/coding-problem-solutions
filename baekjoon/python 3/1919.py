# 문제 링크: https://www.acmicpc.net/problem/1919

s1, s2 = input(), input()

c1, c2 = [0] * 26, [0] * 26
for ch in s1:
    c1[ord(ch) - 97] += 1
for ch in s2:
    c2[ord(ch) - 97] += 1

print(sum(abs(i - j) for i, j in zip(c1, c2)))
