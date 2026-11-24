class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        memo = [[-1 for _ in range(n)] for _ in range(n)]

        def word(left, right):
            if right >= n:
                substring = s[left:right + 1]
                return substring in wordDict

            if memo[left][right] != -1:
                return memo[left][right]

            substring = s[left:right + 1]


            # Continue string
            tf = word(left, right + 1)

            # Start new string
            if substring in wordDict:
                tf = word(right + 1, right + 1) or tf

            memo[left][right] = tf
            return tf


        return word(0, 0)
        