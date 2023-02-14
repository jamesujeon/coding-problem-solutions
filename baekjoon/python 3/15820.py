# 문제 링크: https://www.acmicpc.net/problem/15820

import sys
input = sys.stdin.readline

def is_accepted(s):
    for _ in range(s):
        a1, a2 = map(int, input().split())
        if a1 != a2:
            return False
    return True

s1, s2 = map(int, input().split())
if not is_accepted(s1):
    print("Wrong Answer")
    quit()
if not is_accepted(s2):
    print("Why Wrong!!!")
    quit()
print("Accepted")
