# 문제 링크: https://www.acmicpc.net/problem/16017

digits = [input() for _ in range(4)]

print('ignore' if digits[0] in '89' and digits[-1] in '89' and digits[1] == digits[2] else 'answer')
