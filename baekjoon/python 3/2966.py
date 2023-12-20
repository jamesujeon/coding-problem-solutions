# 문제 링크: https://www.acmicpc.net/problem/2966

input()
s = input()

p = (['Adrian', 'ABC', 0], ['Bruno', 'BABC', 0], ['Goran', 'CCAABB', 0])
for i in range(len(s)):
    for j in range(3):
        if s[i] == p[j][1][i % len(p[j][1])]:
            p[j][2] += 1

m = max(p[i][2] for i in range(3))
print(m)

for i in range(3):
    if p[i][2] == m:
        print(p[i][0])
