# 문제 링크: https://www.acmicpc.net/problem/15080

sh, sm, ss = map(int, input().split(' : '))
eh, em, es = map(int, input().split(' : '))

st = (sh * 3600 + sm * 60 + ss)
et = (eh * 3600 + em * 60 + es)
if et < st:
    et += 3600 * 24

print(et - st)
