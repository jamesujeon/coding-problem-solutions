# 문제 링크: https://level.goorm.io/exam/49066/%EA%B1%B0%EC%9A%B8-%EB%8B%A8%EC%96%B4/quiz/1

import sys
input = sys.stdin.readline

words = [input().rstrip() for _ in range(int(input()))]


mappings = {
    'b': 'd', 'd': 'b', 'i': 'i', 'l': 'l', 'm': 'm',
    'n': 'n', 'o': 'o', 'p': 'q', 'q': 'p', 's': 'z',
    'u': 'u', 'v': 'v', 'w': 'w', 'x': 'x', 'z': 's'
}

def is_mirror_word(word):
    if any(ch not in mappings for ch in word):
        return False

    return all(mappings[word[i]] == word[-(i + 1)] for i in range(len(word) // 2 + 1))


for word in words:
    print('Mirror' if is_mirror_word(word) else 'Normal')
