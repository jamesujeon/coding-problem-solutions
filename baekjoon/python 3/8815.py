# 문제 링크: https://www.acmicpc.net/problem/8815

for _ in range(int(input())):
    N = int(input())

    print('ABCBCDCDADAB'[(N - 1) % 12])
