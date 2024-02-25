# 문제 링크: https://www.acmicpc.net/problem/5218

for _ in range(int(input())):
    print('Distances:', *[(ord(y) - ord(x)) % 26 for x, y in zip(*input().split())])
