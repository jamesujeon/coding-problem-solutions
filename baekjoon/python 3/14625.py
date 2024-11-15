# 문제 링크: https://www.acmicpc.net/problem/14625

H1, M1 = map(int, input().split())
H2, M2 = map(int, input().split())
N = input()

m1 = H1 * 60 + M1
m2 = H2 * 60 + M2
c = 0
while m1 <= m2:
    c += N in f'{m1 // 60:02d}{m1 % 60:02d}'
    m1 += 1

print(c)
