# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/42577

def solution(phone_book):
    phone_book.sort(key=len)
    for i in range(len(phone_book) - 1):
        for j in range(i + 1, len(phone_book)):
            if phone_book[j].startswith(phone_book[i]):
                return False
    return True