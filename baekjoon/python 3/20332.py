# 문제 링크: https://www.acmicpc.net/problem/20332

input()
print(("no", "yes")[sum(map(int, input().split())) % 3 == 0])
