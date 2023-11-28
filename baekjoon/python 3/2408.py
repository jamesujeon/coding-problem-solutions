# 문제 링크: https://www.acmicpc.net/problem/2408

print(eval(''.join(input() for _ in range(int(input()) * 2 - 1)).replace('/', '//')))
