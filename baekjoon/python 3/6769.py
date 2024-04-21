# 문제 링크: https://www.acmicpc.net/problem/6769

s = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
n = input()

def f(i):
    a = int(n[i]) * s[n[i + 1]]
    if i < len(n) - 3 and s[n[i + 1]] < s[n[i + 3]]:
        a *= -1
    return a

print(sum(map(f, range(0, len(n), 2))))
