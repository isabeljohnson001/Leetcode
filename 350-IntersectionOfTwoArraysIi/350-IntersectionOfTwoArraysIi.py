# Last updated: 10/8/2025, 9:50:57 PM
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        '''
        nums1.sort()
        nums2.sort()
        i,j=0,0
        res=[]
        while i<len(nums1) and j<len(nums2):
            if nums1[i]==nums2[j]:
                res.append(nums1[i])
                i+=1
                j+=1
            elif nums1[i]<nums2[j]:
                i+=1
            else:
                j+=1
        return res
        '''
        if len(nums1)>len(nums2):
            nums1,nums2=nums2,nums1
        
        hs=defaultdict(int)

        for num in nums1:
            hs[num]+=1
        res=[]
        for num in nums2:
            if hs[num]>0:
                hs[num]-=1
                res.append(num)
        return res
        