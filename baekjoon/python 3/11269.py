# 문제 링크: https://www.acmicpc.net/problem/11269

s = input()
print(sum(s[i] != 'PER'[i % 3] for i in range(len(s))))
