# 문제 링크: https://www.acmicpc.net/problem/14724

input()
c = [max(map(int, input().split())) for _ in range(9)]
print(['PROBRAIN', 'GROW', 'ARGOS', 'ADMIN', 'ANT', 'MOTION', 'SPG', 'COMON', 'ALMIGHTY'][c.index(max(c))])
