# 문제 링크: http://codeforces.com/problemset/problem/131/A

string = input()

if len(string) == 1 or string[1:].isupper():
  string = string.swapcase()

print(string)