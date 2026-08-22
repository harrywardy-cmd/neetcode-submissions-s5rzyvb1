class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        seen = {}
        
        for i in range(len(nums)):
            if nums[i] not in seen:
                seen[nums[i]] = 0
            else:
                seen[nums[i]] = seen[nums[i]] + 1

        max_key = max(seen, key=seen.get)
        print(max_key)

        return max_key
