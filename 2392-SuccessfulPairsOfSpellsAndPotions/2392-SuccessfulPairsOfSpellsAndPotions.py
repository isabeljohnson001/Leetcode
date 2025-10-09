# Last updated: 10/8/2025, 9:47:53 PM
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        
        potions.sort()
        ans=[]

        for spell in spells:

            l,r=0,len(potions)-1
            i=len(potions)
            while l<=r:
                mid=(r+l)//2
                cal=spell*potions[mid]
                if cal>=success:
                    r=mid-1
                    i=mid
                else:
                    l=mid+1
            ans.append(len(potions)-i)
        return ans
