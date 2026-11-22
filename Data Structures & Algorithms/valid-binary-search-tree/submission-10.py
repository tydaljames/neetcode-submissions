# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        if (root.left and self.dfs(root.left)[1] >= root.val) or (root.right and self.dfs(root.right)[0] <= root.val):
            return False

        return True

    def dfs(self, root):
        # print(root.val, root.left.val if root.left else None, root.right.val if root.right else None)

        if root.left:
            left = self.dfs(root.left)
            if left[1] >= root.val:
                left = (float('-inf'), float('inf'))
        else:
            left = (root.val, root.val)

        if root.right:
            right = self.dfs(root.right)
            if right[0] <= root.val:
                right = (float('-inf'), float('inf'))
        else:
            right = (root.val, root.val)

        # print(left, right)

        minVal = min(left[0], right[0])
        maxVal = max(left[1], right[1])
        # print(root.val, left, right)
        

        return (minVal, maxVal)
            

