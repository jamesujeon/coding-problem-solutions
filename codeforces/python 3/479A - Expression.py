# 문제 링크: http://codeforces.com/problemset/problem/479/A

a, b, c = int(input()), int(input()), int(input())

# (a + b) * c = a * c + b * c >= a + b * c => a + b * c 수식은 고려하지 않아도 됌
# a * (b + c) = a * b + a * c >= a * b + c => a * b + c 수식은 고려하지 않아도 됌
print(max((a + b) * c, a * (b + c), a + b + c, a * b * c))