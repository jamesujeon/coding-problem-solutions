# 문제 링크: https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        self.cloned_target = None
        def dfs(root: TreeNode) -> TreeNode:
            if not root or self.cloned_target:
                return
            if root.val == target.val:
                self.cloned_target = root
                return
            dfs(root.left)
            dfs(root.right)

        dfs(cloned)
        return self.cloned_target