# 문제 링크: https://www.acmicpc.net/problem/5236

for _ in range(int(input())):
    s = input()[::-1]

    i = 1
    while i < len(s) and s[i] > s[i - 1]:
        i += 1

    print(f'The longest decreasing suffix of {s[::-1]} is {s[:i][::-1]}')
