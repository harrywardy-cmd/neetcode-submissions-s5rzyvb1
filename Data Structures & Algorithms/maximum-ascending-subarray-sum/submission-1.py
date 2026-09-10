class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        result = nums[0]
        temp = 0
        bruh = 0

        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                result += nums[i]
            else:
                temp =  result
                result = nums[i]
            bruh = max(temp, result,bruh)



        return bruh


        