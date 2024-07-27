# 문제 링크: https://www.acmicpc.net/problem/10262

p1 = sum(map(int, input().split()))
p2 = sum(map(int, input().split()))

if p1 > p2:
    print('Gunnar')
elif p1 < p2:
    print('Emma')
else:
    print('Tie')
