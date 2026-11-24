class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)

        curMin, curMax = 1, 1
        totalMax = nums[0]

        for num in nums:
            if num == 0:
                curMax, curMin = 1, 1
                totalMax = max(0, totalMax)
                continue
            # elif num > 0:
            else:
                curMax, curMin = max(curMax * num, curMin * num, num), min(curMax * num, curMin * num, num)

                # print(num, curMax, curMin)

            totalMax = max(totalMax, curMax)

        return totalMax