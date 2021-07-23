# 문제 링크: https://level.goorm.io/exam/43094/%EC%8B%9C%ED%97%98%EC%84%B1%EC%A0%81-%ED%8F%89%EA%B7%A0%EA%B3%BC-%EB%93%B1%EA%B8%89-%EA%B5%AC%ED%95%98%EA%B8%B0/quiz/1

scores = list(map(int, input().split(' ')))

average = sum(scores) / len(scores)

if average >= 90:
    grade = 'A'
elif average >= 80:
    grade = 'B'
elif average >= 70:
    grade = 'C'
elif average >= 60:
    grade = 'D'
else:
    grade = 'F'

print('{0:.2f} {1}'.format(average, grade))