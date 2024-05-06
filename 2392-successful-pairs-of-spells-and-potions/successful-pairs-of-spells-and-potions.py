class Solution(object):
     
        
    def successfulPairs(self, spells, potions, success):
        
        def binary_search(arr,target):
            left=0
            right=len(arr)-1
            while left<=right:
                mid=(left+right)//2
                num=arr[mid]
                if target<num:
                    right=mid-1
                else:
                    left=mid+1
            return left
        
        # Sort the potions array
        m = len(potions)
        potions.sort()
        ans = []
        
        # For each spell, calculate the required minimum potion strength and perform a binary search
        for spell in spells:
            required_strength = (success + spell - 1) // spell  # Equivalent to math.ceil(success / spell)
            # Find the index where potions are >= required_strength
            i = bisect.bisect_left(potions, required_strength)
            ans.append(m - i)  # Count how many potions have enough strength
        
        return ans