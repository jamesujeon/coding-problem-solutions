# 문제 링크: https://www.acmicpc.net/problem/1371

counts = [0] * 26
while True:
    try:
        for ch in input().replace(" ", ""):
            counts[ord(ch) - 97] += 1
    except EOFError:
        break

max_count = max(counts)
print(''.join(chr(i + 97) for i in range(26) if counts[i] == max_count))
