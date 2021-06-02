# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/17687

def solution(n, t, m, p):
    s = ''
    i = 0
    while len(s) < t * m:
        s += based(i, n)
        i += 1

    return ''.join(s[i] for i in range(p - 1, t * m, m))

def based(n, base):
    if not n:
        return '0'

    nums = '0123456789ABCDEF'
    result = ''
    while n:
        result += nums[n % base]
        n //= base

    return result[::-1]