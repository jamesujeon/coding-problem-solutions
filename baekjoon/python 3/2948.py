# 문제 링크: https://www.acmicpc.net/problem/2948

D, M = map(int, input().split())

wd = ["Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday"]
md = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

print(wd[(sum(md[:M - 1]) + D) % 7])
