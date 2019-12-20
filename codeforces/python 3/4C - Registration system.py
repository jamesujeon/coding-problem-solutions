# 문제 링크: http://codeforces.com/problemset/problem/4/C

n = int(input())
names = [input() for _ in range(n)]

name_dict = dict()
for i, name in enumerate(names):
  if name in name_dict:
    names[i] += str(name_dict[name])
    name_dict[name] += 1
  else:
    names[i] = "OK"
    name_dict[name] = 1

for name in names:
  print(name)