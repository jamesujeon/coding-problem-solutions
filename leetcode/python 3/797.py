# 문제 링크: https://leetcode.com/problems/all-paths-from-source-to-target/

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        N, paths = len(graph), []
        def find_path(path: List[int], next_nodes: List[int]):
            if not next_nodes:
                return
            for node in next_nodes:
                new_path = path + [node]
                if node == N - 1:
                    paths.append(new_path)
                else:
                    find_path(new_path, graph[node])

        find_path([0], graph[0])
        return paths