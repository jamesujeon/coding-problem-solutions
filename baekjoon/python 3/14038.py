# 문제 링크: https://www.acmicpc.net/problem/14038

win_count = sum(input() == 'W' for _ in range(6))

if win_count > 4:
    print(1)
elif win_count > 2:
    print(2)
elif win_count > 0:
    print(3)
else:
    print(-1)
