# 문제 링크: https://www.acmicpc.net/problem/13939

input()
S = input()[:-1].replace('?', '.').replace('!', '.').split('.')
for s in S:
    print(sum(w.isalpha() and w[0].isupper() for w in s.split()))
