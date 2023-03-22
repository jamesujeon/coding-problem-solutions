# 문제 링크: https://www.acmicpc.net/problem/17614

count = 0
for i in range(3, int(input()) + 1):
    i = str(i)
    count += i.count('3') + i.count('6') + i.count('9')

print(count)
