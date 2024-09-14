# 문제 링크: https://www.acmicpc.net/problem/11608

c = [0] * 26
for i in input():
    c[ord(i) - 97] += 1

print(sum(sorted(c)[:-2]))
