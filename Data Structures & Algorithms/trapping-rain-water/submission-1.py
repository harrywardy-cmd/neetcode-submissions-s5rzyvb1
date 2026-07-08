class Solution:
    def trap(self, height: List[int]) -> int:
        L, R = 0, len(height) - 1

        left_Max, right_Max = height[L], height[R]
        result = 0
        
        while L < R:
            if left_Max < right_Max:
                L += 1
                left_Max = max(left_Max, height[L])
                result += left_Max - height[L]
            else:
                R -= 1
                right_Max = max(right_Max, height[R])
                result += right_Max - height[R]
        return result

