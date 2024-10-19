# 문제 링크: https://www.acmicpc.net/problem/13772

for _ in range(int(input())):
    s = input()
    print(sum(s.count(i) for i in 'ABBDOPQR'))
