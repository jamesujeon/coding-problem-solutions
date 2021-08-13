# 문제 링크: https://www.acmicpc.net/problem/1764

import sys
input = sys.stdin.readline
print = sys.stdout.write

N, M = map(int, input().split())
n_list = set(input().rstrip() for _ in range(N))
m_list = set(input().rstrip() for _ in range(M))


nm_list = sorted(n_list & m_list)


print('{}\n{}\n'.format(len(nm_list), '\n'.join(nm_list)))