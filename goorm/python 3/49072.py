# 문제 링크: https://level.goorm.io/exam/49072/1%EB%93%B1%EA%B3%BC-2%EB%93%B1/quiz/1

s = input()


i1 = s.find('12')
i2 = s.find('21')


print('Yes' if (i1 >= 0 and '21' in s[i1 + 2:]) or (i2 >= 0 and '12' in s[i2 + 2:]) else 'No')
