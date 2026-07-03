class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        my_dict = {}

        for i in range(len(nums)):
            check = target - nums[i]

            if check in my_dict:
                return[my_dict[check], i]
            else:
                my_dict[nums[i]] = i



        