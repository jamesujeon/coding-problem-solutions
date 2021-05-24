# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/77885

def solution(numbers):
    return list(map(f, numbers))

def f(x: int) -> int:
    if x % 2:
        bits = 0
        n = x
        while n % 2:
            bits += 1
            n >>= 1
        return x + 2 ** (bits - 1)
    else:
        return x + 1