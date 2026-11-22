# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    maxPath = -sys.maxsize
    # maxSolo = float('inf')

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.maxPath

    def dfs(self, root):
        if not root:
            return 0

        left = max(self.dfs(root.left), 0)
        right = max(self.dfs(root.right), 0)

        cur = root.val
        sum = (left + right + cur)

        self.maxPath = max(sum, self.maxPath)
        return max(left, right) + cur
