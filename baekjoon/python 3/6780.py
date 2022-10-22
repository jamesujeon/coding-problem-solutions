# 문제 링크: https://www.acmicpc.net/problem/6780

t1, t2 = int(input()), int(input())

length = 2
while t1 >= t2:
    t1, t2 = t2, t1 - t2
    length += 1

print(length)
