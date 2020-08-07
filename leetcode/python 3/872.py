# 문제 링크: https://leetcode.com/problems/leaf-similar-trees/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def get_sequence(root: TreeNode) -> List[int]:
            if not root:
                return []
            if not root.left and not root.right:
                return [root.val]
            return get_sequence(root.left) + get_sequence(root.right)

        return get_sequence(root1) == get_sequence(root2)