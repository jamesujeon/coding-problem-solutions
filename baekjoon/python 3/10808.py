# 문제 링크: https://www.acmicpc.net/problem/10808

S = input()

counts = [0] * 26
for ch in S:
    counts[ord(ch) - 97] += 1

print(*counts)
