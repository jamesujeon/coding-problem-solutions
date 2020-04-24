# 문제 링크: https://www.acmicpc.net/problem/10539

input()
b = [0] + list(map(lambda x: int(x[1]) * (x[0] + 1), enumerate(input().split())))
print(' '.join(str(b[i] - b[i - 1]) for i in range(1, len(b))))