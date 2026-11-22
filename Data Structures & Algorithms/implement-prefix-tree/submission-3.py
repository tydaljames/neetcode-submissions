class Node:
    def __init__(self, val="", children=None):
        self.val = val
        self.children = {}


class PrefixTree:

    def __init__(self):
       self.root = Node()
       self.terminator = Node("$")

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                child = Node(char)
                node.children[char] = child
            node = node.children[char]
        node.children["$"] = self.terminator
        
    def search(self, word: str) -> bool:
        node = self.root

        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
            # print(node.children)


        return "$" in node.children

    def startsWith(self, prefix: str) -> bool:
        node = self.root

        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
        