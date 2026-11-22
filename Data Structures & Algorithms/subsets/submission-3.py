class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.sets = [[]]

        def backtrack(seen, i):
            if i >= len(nums):
                return
            seen.append(nums[i])
            self.sets.append(seen.copy())

            take = backtrack(seen, i + 1)
            seen.pop()
            skip = backtrack(seen, i + 1)

        backtrack([], 0)

        return self.sets