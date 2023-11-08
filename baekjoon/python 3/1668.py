# 문제 링크: https://www.acmicpc.net/problem/1668

def f(t):
    count = max_t = 0
    for i in t:
        if i > max_t:
            count += 1
            max_t = i
    print(count)


t = [int(input()) for _ in range(int(input()))]

f(t)
f(t[::-1])
