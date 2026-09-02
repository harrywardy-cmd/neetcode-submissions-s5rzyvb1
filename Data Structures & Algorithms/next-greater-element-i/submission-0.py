class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1Temp = {num : i for i, num in enumerate(nums1)}
        ans = [-1] * len(nums1)

        for i in range(len(nums2)):
            if nums2[i] not in nums1Temp:
                continue
            for j in range(i + 1, len(nums2)):
                if nums2[j] > nums2[i]:
                    temp = nums1Temp[nums2[i]]
                    ans[temp] = nums2[j]
                    break
        return ans