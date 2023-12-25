# 문제 링크: https://www.acmicpc.net/problem/3181

b = ('i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili')
w = input().split()

print(''.join(w[i][0].upper() for i in range(len(w)) if i == 0 or w[i] not in b))
