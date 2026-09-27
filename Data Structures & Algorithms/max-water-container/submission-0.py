class Solution:
    def maxArea(self, heights: List[int]) -> int:
        output = 0
        
        #Make two pointers
        left = 0
        right = len(heights) -  1

        #chose heighest numbers as far as possible

        while left < right:
            area = 0
            min_height = min(heights[left], heights[right])
            #Calculate the area
            area = (right - left) * min_height
            
            #If the result is the higher than existing output, store it as output
            if area > output:
                output = area

            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1

        return output