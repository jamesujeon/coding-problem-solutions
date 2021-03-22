# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/49993

def solution(skill, skill_trees):
    skill_trees = [
        ''.join(filter(lambda x: x in skill, tree)) 
        for tree in skill_trees
    ]
    return sum(skill.startswith(tree) for tree in skill_trees)