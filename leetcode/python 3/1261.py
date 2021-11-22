# 문제 링크: https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.elements = set()
        
        def init_elements(node: Optional[TreeNode], val: int):
            if not node:
                return

            self.elements.add(val)
            init_elements(node.left, 2 * val + 1)
            init_elements(node.right, 2 * val + 2)

        init_elements(root, 0)

    def find(self, target: int) -> bool:
        return target in self.elements


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)