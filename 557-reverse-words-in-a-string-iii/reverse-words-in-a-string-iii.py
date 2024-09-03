class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        arr=s.split(' ')
        left=0
        right=0
        for i in range(len(arr)):
            curr_word=arr[i]
            arr[i] = curr_word[::-1] 
        return ' '.join(arr)
        