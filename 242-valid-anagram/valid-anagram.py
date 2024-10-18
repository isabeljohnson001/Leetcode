from collections import Counter
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_counts=Counter(s)
        t_counts=Counter(t)
        return s_counts==t_counts
        