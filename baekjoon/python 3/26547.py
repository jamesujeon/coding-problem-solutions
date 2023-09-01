# 문제 링크: https://www.acmicpc.net/problem/26547

for _ in range(int(input())):
    s = input()
    k = len(s)

    print(s)
    if k > 1:
        for i in range(1, k - 1):
            print(s[i] + ' ' * (k - 2) + s[k - i - 1])
        print(s[::-1])
