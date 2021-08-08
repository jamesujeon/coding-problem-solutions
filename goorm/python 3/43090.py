# 문제 링크: https://level.goorm.io/exam/43090/%EB%8C%80%EC%86%8C%EB%AC%B8%EC%9E%90-%EB%B0%94%EA%BE%B8%EC%96%B4-%EC%B6%9C%EB%A0%A5%ED%95%98%EA%B8%B0/quiz/1

s = input()

print(''.join(ch.lower() if ch.isupper() else ch.upper() for ch in s))