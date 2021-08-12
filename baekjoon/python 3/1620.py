# 문제 링크: https://www.acmicpc.net/problem/1620

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

pokemons, pokemon_nums = [], {}
for i in range(N):
    name = input().rstrip()
    pokemons.append(name)
    pokemon_nums[name] = str(i + 1)


answers = []
for _ in range(M):
    problem = input().rstrip()
    if problem.isdigit():
        answers.append(pokemons[int(problem) - 1])
    else:
        answers.append(pokemon_nums[problem])


print('\n'.join(answers))