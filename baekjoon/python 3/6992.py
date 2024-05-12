# 문제 링크: https://www.acmicpc.net/problem/6992

for _ in range(int(input())):
    n, *s = map(int, input().split())

    d = s[1] - s[0]
    if all(i - j == d for i, j in zip(s[2:], s[1:])):
        print(f"The next 5 numbers after {s} are: {[s[-1] + i * d for i in range(1, 6)]}")
    else:
        print(f"The sequence {s} is not an arithmetic sequence.")
