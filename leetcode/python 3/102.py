# 문제 링크: https://leetcode.com/problems/binary-tree-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root or root.val is None:
            return []

        values = []
        q = [root]
        while q:
            level_values = []
            for _ in range(len(q)):
                node = q.pop(0)
                level_values.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            values.append(level_values)

        return values