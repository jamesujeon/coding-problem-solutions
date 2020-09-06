# 문제 링크: https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.k = k
        self.result = 0
        def dfs(node: TreeNode):
            if not node or self.result:
                return
            dfs(node.left)
            self.k -= 1
            if not self.k:
                self.result = node.val
            dfs(node.right)

        dfs(root)
        return self.result