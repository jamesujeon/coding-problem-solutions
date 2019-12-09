# 문제 링크: http://codeforces.com/problemset/problem/266/A

n, s = int(input()), input()

result = sum(prev_stone == stone for prev_stone, stone in zip(s[1:], s))

print(result)