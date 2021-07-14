# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/43163

def solution(begin, target, words):
    if target not in words:
        return 0
    if begin == target:
        return 1

    counts = []
    for i in range(len(words)):
        if is_convertable(begin, words[i]):
            counts.append(1 + solution(words[i], target, words[:i] + words[i + 1:]))

    return min(counts) if counts else 0

def is_convertable(begin, target):
    count = 0
    for i in range(len(begin)):
        if begin[i] != target[i]:
            count += 1
            if count > 1:
                return False
    return True