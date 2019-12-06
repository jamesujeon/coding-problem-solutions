# 문제 링크: http://codeforces.com/problemset/problem/282/A

n = int(input())
stmts = list(map(lambda x: x.replace('X', ''), [input() for i in range(n)]))

x = sum(1 if stmt == '++' else -1 for stmt in stmts)

print(x)