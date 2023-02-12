# 문제 링크: https://www.acmicpc.net/problem/5292

for i in range(1, int(input()) + 1):
    if i % 15 == 0:
        print("DeadMan")
    elif i % 3 == 0:
        print("Dead")
    elif i % 5 == 0:
        print("Man")
    else:
        print(i, end=' ')
