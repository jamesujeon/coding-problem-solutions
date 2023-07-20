# 문제 링크: https://www.acmicpc.net/problem/25813

s = input()
i, j = s.find('U'), s.rfind('F')

print(f"{'-' * i}U{'C' * (j - i - 1)}F{'-' * (len(s) - j - 1)}")
