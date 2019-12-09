# 문제 링크: http://codeforces.com/problemset/problem/281/A

word = input()

if word[0].islower():
  word = word[0].upper() + word[1:]

print(word)