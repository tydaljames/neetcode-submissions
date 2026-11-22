class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        mappings = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        n = len(digits)

        sets = []
        for digit in digits:
            sets.append(mappings[digit])

        combos = []
        combo = []

        def dfs(i):
            if i == n:
                combos.append("".join(combo))
                return 
            
            for j in range(len(sets[i])):
                char = sets[i][j]
                combo.append(char)
                dfs(i + 1)
                combo.pop() 

        
        dfs(0)
        return combos