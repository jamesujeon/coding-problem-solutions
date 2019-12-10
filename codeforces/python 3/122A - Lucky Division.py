# 문제 링크: http://codeforces.com/problemset/problem/122/A

import re

num = int(input())

regex = re.compile(r'^[4,7]+$')
lucky_nums = [i for i in range(1, 1001) if regex.match(str(i))]

print('YES' if any(num % lucky_num == 0 for lucky_num in lucky_nums) else 'NO')