# 문제 링크: http://codeforces.com/problemset/problem/546/A

k, n, w = map(int, input().split())

# borrow_money = max(0, sum(i * k for i in range(1, w + 1)) - n)
borrow_money = max(0, int(w * (w + 1) / 2) * k - n)

print(borrow_money)