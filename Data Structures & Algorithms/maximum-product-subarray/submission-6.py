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
                tempMax = curMax
                curMax = max(curMax * num, curMin * num, num)
                curMin = min(tempMax * num, curMin * num, num)

            totalMax = max(totalMax, curMax)

        return totalMax