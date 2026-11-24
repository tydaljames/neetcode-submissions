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

            memo[left][right] = word(left, right + 1)

            substring = s[left:right + 1]

            if substring in wordDict:
                memo[left][right] = word(right + 1, right + 1) or memo[left][right]

            return memo[left][right]


        return word(0, 0)
        