class Node:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Node()

        found = set()

        rows = len(board)
        cols = len(board[0])

        for word in words:
            node = root

            for char in word:
                if char not in node.children:
                    node.children[char] = Node()
                node = node.children[char]
            node.endOfWord = True

        def find(row, col, node, word):
            # Out of bounds
            if row < 0 or row >= rows or col < 0 or col >= cols or moved[row][col] == True:
                return

            moved[row][col] = True
            char = board[row][col]
            word.append(char)

            # Found match
            if char in node.children:
                node = node.children[char]

                if node.endOfWord:
                    wordStr = "".join(word)
                    if wordStr not in found:
                        found.add(wordStr)

                if node.children:
                    find(row, col + 1, node, word)
                    find(row + 1, col, node, word)
                    find(row, col - 1, node, word)
                    find(row - 1, col, node, word)
           
            moved[row][col] = False
            word.pop()


        moved = [[False for _ in range(cols)] for _ in range(rows)] 

        for row in range(rows):
            for col in range(cols):
                find(row, col, root, [])
        return list(found)
