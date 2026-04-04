class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        self.target = target
        self.nums = nums

        my_hash_map = {}

        for x in range(len(nums)):
            my_hash_map[nums[x]] = x

        for x in range(len(nums)):
            y = target - nums[x]
            if y in my_hash_map and my_hash_map[y] != x:
                return [x,my_hash_map[y]]

        return [0,0]
                





        

            

        

