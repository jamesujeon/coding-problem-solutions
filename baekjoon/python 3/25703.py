# 문제 링크: https://www.acmicpc.net/problem/25703

N = int(input())

print("int a;")
a, b = "ptr", "a"
for i in range(1, N + 1):
    print(f"int {'*' * i}{a} = &{b};")
    a, b = f"ptr{i + 1}", a
