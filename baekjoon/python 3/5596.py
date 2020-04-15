# 문제 링크: https://www.acmicpc.net/problem/5596

s = sum(map(int, input().split()))
t = sum(map(int, input().split()))

print(s if s >= t else t)