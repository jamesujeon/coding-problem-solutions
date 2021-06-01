# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/17686

import re

def solution(files):
    def key(file):
        h, n, _ = re.match(r'([a-z .-]+)(\d{1,5})(.*)', file.lower()).groups()
        return (h, int(n))

    return sorted(files, key=key)