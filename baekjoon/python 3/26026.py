# 문제 링크: https://www.acmicpc.net/problem/26026

n = int(input())
s = input()

print(n - s.replace("10", "1").replace("10", "").count("0"))
