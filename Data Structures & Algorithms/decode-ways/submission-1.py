class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        memo = [-1 for _ in range(n)]

        def decode(i):
            if i >= n:
                return 1
            if memo[i] > -1:
                return memo[i]
            if s[i] == "0":
                return 0

            memo[i] = decode(i + 1)

            if (i + 1 < n and 
                (s[i] == "1" or 
                (s[i] == "2" and s[i + 1] <= "6"))):
                memo[i] += decode(i + 2)

            return memo[i]

        ways = decode(0)
        return ways
        