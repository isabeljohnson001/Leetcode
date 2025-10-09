# Last updated: 10/8/2025, 9:48:48 PM
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:

        boxTypes.sort(key=lambda x: -x[1])

        curr_size=0
        max_units=0
        for num_box,units in boxTypes:
            max_units+=units* min(num_box,truckSize-curr_size)
            curr_size+=min(num_box,truckSize-curr_size)
        return max_units

        