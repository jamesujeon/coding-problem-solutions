# 문제 링크: https://www.acmicpc.net/problem/14991

input()
b = 1
for i in map(int, input().split()):
    b = (b * 2 - i)
    if b < 0:
        print('error')
        break
else:
    print(b % (10**9 + 7))
