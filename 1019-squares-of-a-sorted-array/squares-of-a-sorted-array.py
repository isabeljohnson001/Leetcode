class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i = 0
        j = len(nums) - 1
        result = [0] * len(nums)  # Preallocate the result array for better efficiency
        k = len(nums) - 1         # Start filling the result from the end

        while i <= j:
            if abs(nums[i]) > abs(nums[j]):
                result[k] = nums[i] ** 2
                i += 1
            else:
                result[k] = nums[j] ** 2
                j -= 1
            k -= 1

        return result
        