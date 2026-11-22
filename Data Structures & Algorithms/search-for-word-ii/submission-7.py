class Node:
    def __init__(self, char=""):
        self.char = char
        self.children = {}
        self.endOfWord = False

        # ["o","a","a","n"]
        # ["e","t","a","e"]
        # ["i","h","k","r"]
        # ["i","f","l","v"]

        # ["o","a","b","n"],
        # ["o","t","a","e"],
        # ["a","h","k","r"],
        # ["a","f","l","v"]

        # ["o","a","a","n"],
        # ["e","t","a","e"],
        # ["i","h","k","r"],
        # ["i","f","l","v"]

        # ["a","b","c"],
        # ["a","e","d"],
        # ["a","f","g"]

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        print = lambda *args, **kwargs: None
        root = Node()

        found = set()

        rows = len(board)
        cols = len(board[0])

        for word in words:
            node = root

            for char in word:
                if char not in node.children:
                    node.children[char] = Node(char)
                node = node.children[char]
                
            node.endOfWord = True


        def find(row, col, node, word):
            # Out of bounds
            if row < 0 or row >= rows or col < 0 or col >= cols or moved[row][col] == True:
                return

            moved[row][col] = True
            char = board[row][col]
            word.append(char)
            print(row, col, char, word)

            # Found match
            if char in node.children:
                node = node.children[char]

                if node.endOfWord:
                    wordStr = "".join(word)
                    if wordStr not in found:
                        found.add(wordStr)

                find(row, col + 1, node, word)
                find(row + 1, col, node, word)
                find(row, col - 1, node, word)
                find(row - 1, col, node, word)

            # No match, keep moving
                # Exit if node has no children
                # Exit if word too large

                # if not node.children:
                    # print("Early exit on:", char)



            moved[row][col] = False
            word.pop()



        for row in range(rows):
            for col in range(cols):
                print("Starting at:", row, col)
                moved = [[False for _ in range(cols)] for _ in range(rows)] 
                find(row, col, root, [])
        return list(found)
