# 문제 링크: https://www.acmicpc.net/problem/13587

print('NS'[(s := [c for c in input() if c in 'aeiou']) == s[::-1]])
