# 문제 링크: http://codeforces.com/problemset/problem/208/A

import re

s = input()

print(re.sub(r'(WUB)+', ' ', s).strip())