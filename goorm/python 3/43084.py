# 문제 링크: https://level.goorm.io/exam/43084/happy-number/quiz/1

n = int(input())

records = [n]
while True:
    n = sum(int(i)**2 for i in str(n))

    if n == 1 or n in records:
        print(f"{records[0]} is {'Happy' if n == 1 else 'Unhappy'} Number.")
        break

    records.append(n)