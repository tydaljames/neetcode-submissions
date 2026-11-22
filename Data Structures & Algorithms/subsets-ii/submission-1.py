class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        subs = [[]]

        def dfs(sub, i):
            if i == n:
                return

            for j in range(i, n):
                if j > i and nums[j - 1] == nums[j]:
                    continue

                sub.append(nums[j])
                subs.append(sub.copy())
                dfs(sub, j + 1)
                sub.pop()
                # dfs(sub, i + 1)

        dfs([], 0)
        return subs