# 문제 링크: http://codeforces.com/problemset/problem/118/A

string = input()

vowels = ['a', 'o', 'y', 'e', 'u', 'i']
result = string.lower()
result = ".".join(filter(lambda x: x not in vowels, result))
if len(result) > 0:
  result = '.' + result

print(result)