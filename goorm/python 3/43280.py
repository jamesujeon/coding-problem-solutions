# 문제 링크: https://level.goorm.io/exam/43280/%EC%B1%84%EC%A0%90%ED%95%98%EA%B8%B0/quiz/1

answers = input()

total_score = 0
score = 1
for answer in answers:
    if answer == 'o':
        total_score += score
        score += 1
    else:
        score = 1

print(total_score)