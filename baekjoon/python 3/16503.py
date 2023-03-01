# 문제 링크: https://www.acmicpc.net/problem/16503

K1, O1, K2, O2, K3 = input().split()

R1, R2 = int(eval(f"int({K1}{O1}{K2}){O2}{K3}")), int(eval(f"{K1}{O1}int({K2}{O2}{K3})"))

print(min(R1, R2))
print(max(R1, R2))
