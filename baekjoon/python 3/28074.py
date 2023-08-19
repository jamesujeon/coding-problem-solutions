# 문제 링크: https://www.acmicpc.net/problem/28074

s = input()
print("YES" if all(ch in s for ch in "MOBIS") else "NO")
