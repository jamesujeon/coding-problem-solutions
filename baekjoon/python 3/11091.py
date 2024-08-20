# 문제 링크: https://www.acmicpc.net/problem/11091

for _ in range(int(input())):
    s = ''.join(sorted(set(map(chr, range(97, 123))) - set(input().lower())))

    print(f"missing {s}" if s else "pangram")
