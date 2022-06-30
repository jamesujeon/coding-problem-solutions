# 문제 링크: https://www.acmicpc.net/problem/18409

_, S = input(), input()

print(sum(ch in 'aiueo' for ch in S))
