# 문제 링크: https://www.acmicpc.net/problem/17094

input()
s = input()

counts = (s.count('2'), s.count('e'))
if counts[0] > counts[1]:
    print('2')
elif counts[0] < counts[1]:
    print('e')
else:
    print("yee")
