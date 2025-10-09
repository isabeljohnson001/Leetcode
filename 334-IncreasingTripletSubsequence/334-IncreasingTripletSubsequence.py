# Last updated: 10/8/2025, 9:51:03 PM
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        first_num=float("inf")
        second_num=float("inf")

        for n in nums:
            if n<=first_num:
                first_num=n
            elif n<=second_num:
                second_num=n
            else:
                return True
        return False
        