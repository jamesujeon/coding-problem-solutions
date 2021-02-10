# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/42746

def solution(numbers):
    def get_key(s: str) -> (str, int):
        filled = (s + s[:4 - len(s)]) if len(s) > 1 else s.ljust(4, s[0])
        return (filled, -len(s))

    result = ''.join(sorted(map(str, numbers), key=get_key, reverse=True))
    return result if any(ch != '0' for ch in result) else '0'