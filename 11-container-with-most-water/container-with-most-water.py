class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0
    
        while left < right:
            # Calculate the current area between left and right
            current_area = (right - left) * min(height[left], height[right])
            max_area = max(max_area, current_area)
            
            # Move the pointer for the shorter line inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_area
        