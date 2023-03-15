# 문제 링크: https://www.acmicpc.net/problem/17042

W = input()
wizards = set(W)
for _ in range(int(input())):
    Z1, Z2 = input().split()
    if Z2 == W:
        W = Z1
        wizards.add(W)

print(W)
print(len(wizards))
