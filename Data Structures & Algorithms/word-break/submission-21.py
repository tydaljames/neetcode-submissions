class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        memo = [-1 for _ in range(n)]
        minWord = float('inf')
        maxWord = 0

        for word in wordDict:
            minWord = min(len(word), minWord)
            maxWord = max(len(word), maxWord)

        def word(left):
            if left >= n:
                return True

            if memo[left] != -1:
                return memo[left]
            
            for right in range(left + minWord, n + 1):
                if (right - left) > maxWord:
                    break

                substring = s[left:right]
                if substring in wordDict:
                    if word(right):
                        memo[left] = True
                        return memo[left]
                    # memo[left] = word(right) or memo[left]

                    # if memo[left] == True:
                    #     return memo[left]

            memo[left] = False
            return memo[left]


        return word(0)
        