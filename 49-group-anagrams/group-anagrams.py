
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hs=collections.defaultdict(list)
        for s in strs:
            counter=[0]*26
            for c in s:
                counter[ord(c)-ord("a")]+=1
            hs[tuple(counter)].append(s)
        return hs.values()

