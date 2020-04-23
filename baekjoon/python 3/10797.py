# 문제 링크: https://www.acmicpc.net/problem/10797

d = int(input())
print(sum(i == d for i in map(int, input().split())))