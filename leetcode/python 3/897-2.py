# 문제 링크: https://leetcode.com/problems/increasing-order-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        values = []
        def dfs(node: TreeNode):
            if not node:
                return
            dfs(node.left)
            values.append(node.val)
            dfs(node.right)

        dfs(root)
        
        tree = TreeNode(values[0])
        node = tree
        for i in range(1, len(values)):
            node.right = TreeNode(values[i])
            node = node.right
        return tree