# 문제 링크: https://www.acmicpc.net/problem/8714

n = int(input())
zeros = input().count('0')

print(min(zeros, n - zeros))
