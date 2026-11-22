# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        def dfs(root, serial):
            if not root:
                return

            if root.left:
                serial.append(str(root.left.val))
            else:
                serial.append(str())

            if root.right:
                serial.append(str(root.right.val))
            else:
                serial.append(str())
            
            dfs(root.left, serial)
            dfs(root.right, serial)
            
        serial = []
        if root:
            serial.append(str(root.val))
        else:
            serial.append(str())


        dfs(root, serial)

        for num in reversed(serial):
            if num == "None":
                serial.pop()
            else:
                break

        send = "$".join(serial)

        return send

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        serial = data.split("$")
        print(serial)

        if len(serial) == 0:
            return None

        root = TreeNode(serial[0])

        i = 1

        def dfs(root, serial):                
            nonlocal i
            if not root or i >= len(serial):
                return

            if serial[i] != "":
                root.left = TreeNode(int(serial[i]))

            i += 1

            if i < len(serial) and serial[i] != "":
                root.right = TreeNode(int(serial[i]))
            i += 1


            dfs(root.left, serial)
            dfs(root.right, serial)

        dfs(root, serial)
        return root
