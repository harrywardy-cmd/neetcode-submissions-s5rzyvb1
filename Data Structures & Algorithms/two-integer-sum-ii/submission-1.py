class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L,R = 0,len(numbers) - 1

        while L<R:
            if numbers[R] + numbers[L] < target:
                L += 1
            if numbers[R] + numbers[L] > target:
                R -= 1
            if numbers[R] + numbers[L] == target:
                return [L+1,R+1]
        return 0