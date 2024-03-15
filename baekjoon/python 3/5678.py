# 문제 링크: https://www.acmicpc.net/problem/5678

import sys
input = sys.stdin.readline

while (R := int(input())) != 0:
    M = list(map(int, input().split()))
    L = list(map(int, input().split()))

    m, l = sum(M), sum(L)
    for i in range(R - 2):
        m_flag = M[i] == M[i + 1] == M[i + 2]
        l_flag = L[i] == L[i + 1] == L[i + 2]
        if m_flag or l_flag:
            m += 30 if m_flag else 0
            l += 30 if l_flag else 0
            break

    if m > l:
        print('M')
    elif m < l:
        print('L')
    else:
        print('T')
