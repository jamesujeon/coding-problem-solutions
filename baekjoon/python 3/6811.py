# 문제 링크: https://www.acmicpc.net/problem/6811

p = [int(input()) for _ in range(4)]

c = []
for i in range(p[3] // p[0] + 1):
    for j in range((p[3] - p[0] * i) // p[1] + 1):
        for k in range((p[3] - p[0] * i - p[1] * j) // p[2] + 1):
            if i + j + k > 0:
                c.append((i, j, k))

for i, j, k in c:
    print(f"{i} Brown Trout, {j} Northern Pike, {k} Yellow Pickerel")
print(f"Number of ways to catch fish: {len(c)}")
