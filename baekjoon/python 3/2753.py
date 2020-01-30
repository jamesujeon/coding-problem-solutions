# 문제 링크: https://www.acmicpc.net/problem/2753

y = int(input())
print(int((y % 4 == 0 and y % 100 > 0) or y % 400 == 0))