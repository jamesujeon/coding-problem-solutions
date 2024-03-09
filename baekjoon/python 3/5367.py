# 문제 링크: https://www.acmicpc.net/problem/5367

n = int(input()) - 2

print(f"|{'-' * n}|")
print('\n'.join(f"|{' ' * i}*{' ' * (n - (i + 1) * 2)}*{' ' * i}|" for i in range(n // 2)))
print(f"|{' ' * (n // 2)}*{' ' * (n // 2)}|")
print('\n'.join(f"|{' ' * i}*{' ' * (n - (i + 1) * 2)}*{' ' * i}|" for i in range(n // 2 - 1, -1, -1)))
print(f"|{'-' * n}|")
