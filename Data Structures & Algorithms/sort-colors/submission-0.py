class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colorCounts = [0, 0, 0]

        # Count the quantity of each val in arr
        for n in nums:
            colorCounts[n] += 1
            i = 0
        for n in range(len(colorCounts)):
            for j in range(colorCounts[n]):
                nums[i] = n
                i += 1

