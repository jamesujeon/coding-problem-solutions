# 문제 링크: https://www.acmicpc.net/problem/7572

N = int(input()) - 4
print(f"{chr(N % 12 + 65)}{N % 10}")
