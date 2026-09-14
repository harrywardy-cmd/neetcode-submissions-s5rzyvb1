class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        increase = 1
        decreasing = 1
        result = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                increase = 1
                decreasing = 1
            elif nums[i] > nums[i - 1]:
                increase = increase + 1
                decreasing = 1
            else:
                increase = 1
                decreasing = decreasing + 1

            result = max(result, increase, decreasing)

        return result