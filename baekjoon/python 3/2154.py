# 문제 링크: https://www.acmicpc.net/problem/2154

N = input()
print(''.join(str(i) for i in range(1, int(N) + 1)).find(N) + 1)
