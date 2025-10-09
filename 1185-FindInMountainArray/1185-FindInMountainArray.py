# Last updated: 10/8/2025, 9:49:19 PM
# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class mountainArr:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:

        def binSearch(l,r,asc,target):
            while l<=r:
                m=(l+r)//2
                num=num=mountainArr.get(m)
                if num==target:
                    return m
                if asc:
                    if num<target:
                        l=m+1
                    else:
                        r=m-1
                else:
                    if num<target:
                        r=m-1
                    else:
                        l=m+1
            return -1

        l=0
    
        n=mountainArr.length()
        r=n-1

        while l<=r:

            m=(l+r)//2

            if mountainArr.get(m)<mountainArr.get(m+1):
                l=m+1
            else:
                r=m-1
        peak=l

        idx=binSearch(0,peak,True,target)
        if idx!=-1:
            return idx

        idx=binSearch(peak,n-1,False,target)
        return idx