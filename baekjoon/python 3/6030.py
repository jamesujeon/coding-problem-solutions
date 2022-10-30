# 문제 링크: https://www.acmicpc.net/problem/6030

P, Q = map(int, input().split())

p_div, q_div = set(), set()
for i in range(1, int(max(P, Q)**.5) + 1):
    if P % i == 0:
        p_div.add(i)
        p_div.add(P // i)
    if Q % i == 0:
        q_div.add(i)
        q_div.add(Q // i)

for p in sorted(p_div):
    for q in sorted(q_div):
        print(p, q)
