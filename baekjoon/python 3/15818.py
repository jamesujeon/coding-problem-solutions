# 문제 링크: https://www.acmicpc.net/problem/15818

_, M = map(int, input().split())

result = 1
for i in map(int, input().split()):
    result = (result * (i % M)) % M

print(result)
