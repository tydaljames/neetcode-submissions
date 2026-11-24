class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        memo = [[-1 for _ in range(n)] for _ in range(n)]
        minWord = float('inf')
        maxWord = 0

        for word in wordDict:
            minWord = min(len(word), minWord)
            maxWord = max(len(word), maxWord)

        print(minWord, maxWord)

        def word(left, right):
            if right >= n:
                return s[left:right + 1] in wordDict

            if memo[left][right] != -1:
                return memo[left][right]
            
            if (right - left) + 1 > maxWord:
                memo[left][right] = False
                return memo[left][right]

            memo[left][right] = word(left, right + 1)

            substring = s[left:right + 1]

            if substring in wordDict:
                memo[left][right] = word(right + 1, right + minWord) or memo[left][right]

            return memo[left][right]


        return word(0, 0)
        