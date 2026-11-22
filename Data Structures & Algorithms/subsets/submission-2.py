class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.sets = [[]]

        def backtrack(nums, seen, i):
            if i >= len(nums):
                return
            # print(nums[i:j+1])
            seen.append(nums[i])
            self.sets.append(seen.copy())

            # print(self.sets)

            take = backtrack(nums, seen, i + 1)
            seen.pop()
            skip = backtrack(nums, seen, i + 1)
            # backtrack(nums, i, j + 1)

        backtrack(nums, [], 0)

        return self.sets