# 문제 링크: https://www.acmicpc.net/problem/9228

while (s := input()) != '#':
    d = -(sum(int(s[-i - 1]) * (i + 2) for i in range(len(s))) % -11)

    print(f"{s} -> {d if d < 10 else 'Rejected'}")
