# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/12930

def solution(s):
    def convert(s: str) -> str:
        return ''.join(
            s[i].lower() if i % 2 else s[i].upper()
            for i in range(len(s))
        )

    return ' '.join(map(convert, s.split(' ')))