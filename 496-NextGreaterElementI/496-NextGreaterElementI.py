# Last updated: 10/8/2025, 9:50:45 PM
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        nextGreater={}
        stack=[]
        for x in nums2:
            
            while stack and stack[-1]<x:
                y=stack.pop()
                nextGreater[y]=x
                
            stack.append(x)
        while stack:
            nextGreater[stack.pop()]=-1
            
        return [nextGreater[v] for v in nums1]
    
    6,5,4,3,2,1,7
    