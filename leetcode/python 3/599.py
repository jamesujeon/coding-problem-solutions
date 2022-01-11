# 문제 링크: https://leetcode.com/problems/minimum-index-sum-of-two-lists/

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        indexes1 = {rest: i for i, rest in enumerate(list1)}
        indexes2 = {rest: i for i, rest in enumerate(list2)}

        min_index_sum = len(list1) + len(list2)
        answer = []
        for rest in set(indexes1) & set(indexes2):
            index_sum = indexes1[rest] + indexes2[rest]
            if index_sum < min_index_sum:
                min_index_sum = index_sum
                answer = [rest]
            elif index_sum == min_index_sum:
                answer.append(rest)

        return answer