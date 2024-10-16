# 문제 링크: https://www.acmicpc.net/problem/13462

C = {'R': 'S', 'B': 'K', 'L': 'H'}
s = input()
i = 0
while i < len(s):
    if set(s[i:i + 3]) == set('RBL'):
        print('C', end='')
        i += 3
    else:
        print(C[s[i]], end='')
        i += 1
print()
