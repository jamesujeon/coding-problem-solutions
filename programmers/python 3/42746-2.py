# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/42746

from functools import cmp_to_key

def solution(numbers):
    def compare(a: str, b: str) -> int:
        return int(b + a) - int(a + b)

    result = ''.join(sorted(map(str, numbers), key=cmp_to_key(compare)))
    return str(int(result))