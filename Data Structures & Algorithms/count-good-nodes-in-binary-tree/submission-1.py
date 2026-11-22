# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def find(root: TreeNode, maxVal: int) -> int:
            if not root:
                return 0

            good = 1 if root.val >= maxVal else 0
            maxVal = max(root.val, maxVal)

            left = find(root.left, maxVal)
            right = find(root.right, maxVal)

            return left + right + good

        
        return find(root, float('-inf'))
            

    