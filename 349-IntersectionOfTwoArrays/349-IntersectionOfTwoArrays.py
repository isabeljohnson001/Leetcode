# Last updated: 10/8/2025, 9:50:57 PM
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        nums1.sort()
        nums2.sort()
        i,j=0,0
        intersection=set()
        res=[]
        while i<len(nums1) and j<len(nums2):
            if nums1[i]==nums2[j]:
                intersection.add(nums1[i])
                i+=1
                j+=1
            elif nums1[i]<nums2[j]:
                i+=1
            else:
                j+=1
        for i in intersection:
            res.append(i)
        return res

        