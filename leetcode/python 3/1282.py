# 문제 링크: https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        group_ids = {}
        for i in range(len(groupSizes)):
            if groupSizes[i] not in group_ids:
                group_ids[groupSizes[i]] = []
            group_ids[groupSizes[i]].append(i)

        groups = []
        for size, ids in group_ids.items():
            while ids:
                groups.append(ids[:size])
                ids = ids[size:]
        return groups