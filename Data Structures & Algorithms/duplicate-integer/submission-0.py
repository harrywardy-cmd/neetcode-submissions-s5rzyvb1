class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        checknums = set()

        for x in nums:
            if x in checknums: 
                return True
            checknums.add(x)
        
        return False
        