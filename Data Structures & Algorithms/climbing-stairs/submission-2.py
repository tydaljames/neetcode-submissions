class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [i if i <= 3 else -1 for i in range(n + 1)]

        print(memo)

        def climb(n):
            if memo[n] > -1:
                return memo[n]

            take1 = climb(n - 1)
            take2 = climb(n - 2)

            memo[n] = take1 + take2
            return memo[n]

        return climb(n)