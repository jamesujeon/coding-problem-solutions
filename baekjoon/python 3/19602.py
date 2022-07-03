# 문제 링크: https://www.acmicpc.net/problem/19602

print('happy' if sum(int(input()) * i for i in range(1, 4)) >= 10 else 'sad')
