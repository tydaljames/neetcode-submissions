# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        view = []
        dq = deque([(root, 0)])

        while dq:
            cur = dq.popleft()
            node = cur[0]
            level = cur[1]

            if len(view) <= level:
                view.append(node.val)


            if node.right:
                dq.append((node.right, level + 1))
            if node.left:
                dq.append((node.left, level + 1))

        return view