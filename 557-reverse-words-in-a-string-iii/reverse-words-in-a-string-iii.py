class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        arr=s.split(' ')
        for i in range(len(arr)):
            curr_word=list(arr[i])
            left,right=0,len(curr_word)-1
            while left<right:
                curr_word[left],curr_word[right]=curr_word[right],curr_word[left]
                left+=1
                right-=1
            arr[i]=''.join(curr_word)
        return ' '.join(arr)
            