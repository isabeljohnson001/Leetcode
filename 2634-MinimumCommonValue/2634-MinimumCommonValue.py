# Last updated: 10/8/2025, 9:47:44 PM
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        min_value=float("inf")

        n=len(nums1)
        m=len(nums2)
        left=0
        right=0
        while left<n and right<m:
            if nums1[left]==nums2[right]:
                min_value=min(min_value,nums1[left])
                break
            elif nums1[left]<nums2[right]:
                left+=1
            else:
                right+=1

        return min_value if min_value != float("inf") else -1
        