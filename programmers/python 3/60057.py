# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    return min(map(
        lambda l: len(compress(s, l)),
        range(1, len(s) // 2 + 2)
    ))

def compress(s: str, l: int) -> str:
    result = ''

    i = 0
    while i < len(s):
        count = 0
        substr = s[i:min(i + l, len(s))]
        while i < len(s) and s[i:min(i + l, len(s))] == substr:
            count += 1
            i += l

        result += (str(count) if count > 1 else '') + substr

    return result