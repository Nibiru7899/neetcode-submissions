class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        area = float('-inf')
        while left<right:
            curr_area = (right-left)*min(heights[left],heights[right])
            area = max(area,curr_area)

            if heights[left]<heights[right]:
                left+=1
            else:
                right = right-1
        return area