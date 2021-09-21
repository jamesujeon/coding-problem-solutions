# 문제 링크: https://level.goorm.io/exam/43178/%EC%88%AB%EC%9E%90%EC%B6%9C%EB%A0%A5/quiz/1

for i in range(1, 6):
    print(''.join(str(j + 1) for j in range(i)).zfill(8))
