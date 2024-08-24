# 문제 링크: https://www.acmicpc.net/problem/10420

md = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
y, m, d = 2014, 4, 1 + int(input())

while d > md[m - 1]:
    d, m = d - md[m - 1], m + 1
    if m > 12:
        y, m = y + 1, m - 12
        md[1] = 28 + int((y % 4 == 0 and y % 100 != 0) or y % 400 == 0)

print(f"{y}-{m:02d}-{d:02d}")
