# 문제 링크: https://www.acmicpc.net/problem/9907

print("JABCDEFGHIZ"[sum(int(d) * int(w) for d, w in zip(input(), "2765432")) % 11])
