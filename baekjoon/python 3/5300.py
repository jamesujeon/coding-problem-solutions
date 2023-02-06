# 문제 링크: https://www.acmicpc.net/problem/5300

for i in range(1, int(input()) + 1):
    print(i, end=' ')
    if not i % 6:
        print("Go!", end=' ')

print("Go!" if i % 6 else "")
