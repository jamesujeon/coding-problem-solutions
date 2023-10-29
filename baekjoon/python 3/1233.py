# 문제 링크: https://www.acmicpc.net/problem/1233

S1, S2, S3 = map(int, input().split())

c = {}
for i in range(1, S1 + 1):
    for j in range(1, S2 + 1):
        for k in range(1, S3 + 1):
            s = i + j + k
            if s not in c:
                c[s] = 0
            c[s] += 1

print(max(c, key=c.get))
