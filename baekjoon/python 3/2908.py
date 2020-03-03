# 문제 링크: https://www.acmicpc.net/problem/2908

a, b = input().split()

print(max(int(a[::-1]), int(b[::-1])))