class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curMax = 0
        prevMax = 0

        for i in range(len(nums)):

            if nums[i] == 1:
                curMax +=1
            elif nums[i] == 0:
                prevMax = max(curMax, prevMax)
                curMax = 0

            print("current max",curMax )
            print("previose max",prevMax )

        prevMax = max(curMax, prevMax)
        return prevMax
        