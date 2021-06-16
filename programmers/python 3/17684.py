# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/17684

def solution(msg):
    d = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    def get_w(s: str) -> str:
        return sorted([word for word in d if s.startswith(word)], key=len)[-1]

    i, indices = 0, []
    while i < len(msg):
        w = get_w(msg[i:])
        indices.append(d.index(w) + 1)
        d.append(w + msg[min(i + len(w), len(msg) - 1)])
        i += len(w)

    return indices