# 문제 링크: https://www.acmicpc.net/problem/2941

ca = ('c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=')
s = input()
for c in ca:
  s = s.replace(c, ' ')
print(len(s))