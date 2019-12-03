# 문제 링크: http://codeforces.com/problemset/problem/71/A

n = int(input())
words = [input() for i in range(n)]

abbr_words = []
for word in words:
  if len(word) > 10:
    word = word[0] + str(len(word) - 2) + word[-1]
  abbr_words.append(word)

for word in abbr_words:
  print(word)