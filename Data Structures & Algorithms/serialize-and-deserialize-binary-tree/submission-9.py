# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        serial = []

        def dfs(root):
            if not root:
                serial.append(str())
                return

            serial.append(str(root.val))
            
            dfs(root.left)
            dfs(root.right)
            

        dfs(root)

        # for num in reversed(serial):
        #     if num == "":
        #         serial.pop()
        #     else:
        #         break

        return "$".join(serial)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        serial = data.split("$")
        # print(serial) 

        i = 0

        def dfs():                
            nonlocal i
            if serial[i] == "":
                i += 1
                return None

            root = TreeNode(int(serial[i]))
            i += 1

            root.left = dfs()
            root.right = dfs()
            return root

        dfs()
        return root
