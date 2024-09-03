class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        highest_alt=0
        prefix=[0]
        prefix.append(gain[0])
        highest_alt=max(highest_alt,gain[0])
        for i in range(1,len(gain)):
            diff=prefix[-1]+gain[i]
            prefix.append(diff)
            highest_alt=max(highest_alt,diff)
        return highest_alt