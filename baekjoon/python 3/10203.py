# 문제 링크: https://www.acmicpc.net/problem/10203

for _ in range(int(input())):
    w = input()

    c = sum(i in 'aeiou' for i in w)
    print(f"The number of vowels in {w} is {c}.")