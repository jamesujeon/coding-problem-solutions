# 문제 링크: https://www.acmicpc.net/problem/14954

def f(n):
    return str(sum(map(lambda x: int(x)**2, n)))

n = f(input())
while n not in '14':
    n = f(n)

print(('UN' if n != '1' else '') + 'HAPPY')
