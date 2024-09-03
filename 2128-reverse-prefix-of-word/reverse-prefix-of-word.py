class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        arr=list(word)
        if arr[0]==ch:
            return ''.join(arr) 
        left=0
        right=left+1
        reverse=False
        while left<right and right<len(arr):
            if not reverse:
                if not arr[right]==ch:
                    right+=1
                    continue
                reverse=True
            arr[left],arr[right]=arr[right],arr[left]
            left+=1
            right-=1
            
        return ''.join(arr)

        