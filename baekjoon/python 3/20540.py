# 문제 링크: https://www.acmicpc.net/problem/20540

s = input()

mbti = ["EI", "SN", "TF", "JP"]
print(''.join(mbti[i][(mbti[i].index(s[i]) + 1) % 2] for i in range(len(s))))
