# 문제 링크: https://www.acmicpc.net/problem/4678

while (s := input()[::-1]) != '0':
    print(sum(int(s[i]) * (2**(i + 1) - 1) for i in range(len(s))))
