class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        arr=list(s)
        left=0
        right=len(arr)-1
        while left<right:
            if not arr[left].isalpha():
                left+=1
            if not arr[right].isalpha():
                right-=1
            if arr[left].isalpha() and arr[right].isalpha():
                arr[left],arr[right]=arr[right],arr[left]
                left+=1
                right-=1
        return ''.join(arr)
        