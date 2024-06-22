# 문제 링크: https://www.acmicpc.net/problem/9398

for _ in range(int(input())):
    s = input()

    min_l = 0
    for i in range(len(s) - 5):
        c = [False] * 3
        for j in range(i, len(s)):
            if s[j].isupper():
                c[0] = True
            elif s[j].islower():
                c[1] = True
            elif s[j].isdigit():
                c[2] = True

            if all(c):
                min_l = max(j - i + 1, 6)
                break

    print(min_l)
