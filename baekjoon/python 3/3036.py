# 문제 링크: https://www.acmicpc.net/problem/3036

input()
radiuses = list(map(int, input().split()))

def gcd(a: int, b: int) -> int:
    while a % b > 0:
        a, b = b, a % b
    return b

first_radius = radiuses.pop(0)
for radius in radiuses:
    radius_gcd = gcd(first_radius, radius)
    print(f'{first_radius // radius_gcd}/{radius // radius_gcd}')