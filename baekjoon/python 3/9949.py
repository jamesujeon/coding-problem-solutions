# 문제 링크: https://www.acmicpc.net/problem/9949

i = 1
while (s := input()) != '# #':
    l1, l2 = s.split()

    print(f"Case {i}")
    for _ in range(int(input())):
        print(
            input()
            .replace(l1, '_').replace(l1.upper(), '_')
            .replace(l2, '_').replace(l2.upper(), '_')
        )
    print()
    i += 1
