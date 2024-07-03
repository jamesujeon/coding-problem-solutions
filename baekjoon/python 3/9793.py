# 문제 링크: https://www.acmicpc.net/problem/9793

s = [len(input().split()) for _ in range(int(input()))]
for c in sorted(set(s)):
    print(c, s.count(c))
