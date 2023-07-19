# 문제 링크: https://www.acmicpc.net/problem/25785

is_vowel = [ch in "aeiou" for ch in input()]
for a, b in zip(is_vowel, is_vowel[1:]):
    if a == b:
        print(0)
        break
else:
    print(1)
