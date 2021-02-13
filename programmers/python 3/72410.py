# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/72410

import re

def solution(new_id):
    new_id = new_id.lower()
    new_id = re.sub(r'[^a-z0-9-_.]', '', new_id)
    new_id = re.sub(r'[.]{2,}', '.', new_id)
    new_id = re.sub(r'^[.]|[.]$', '', new_id)
    if new_id:
        new_id = re.sub(r'[.]$', '', new_id[:15])
        if len(new_id) < 3:
            new_id = new_id.ljust(3, new_id[-1])
    else:
        new_id = 'aaa'
    return new_id