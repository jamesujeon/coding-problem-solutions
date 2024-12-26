# 문제 링크: https://www.acmicpc.net/problem/15444

b = [''] * 5
input()
for i in input():
    b[0] += '***'
    b[1] += ['*.*', '*..'][i in 'CE']
    b[2] += ['***', '*..', '*.*'][(i in 'CD') + (i == 'D')]
    b[3] += ['*.*', '*..'][i in 'CE']
    b[4] += ['***', '*.*'][i == 'A']

print('\n'.join(b))
