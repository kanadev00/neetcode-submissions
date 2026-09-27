class Solution:
    def trap(self, height: List[int]) -> int:
        # create total 
        total = 0
        # create a list for the max hight of left side
        leftMax = [0] * len(height)
        # create a number for leftMax[0]
        leftMax[0] = height[0]
        # create rest of the leftMax lists
        for i in range(1, len(height)):
            leftMax[i] = max(height[i], leftMax[i-1])

        # create a list for the max hight of right side
        rightMax = [0] * len(height)
        rightMax[len(height)-1] = height[len(height)-1]

        # create rest of the rightMax lists
        for i in range(len(height)-2, -1, -1):
            rightMax[i] = max(height[i], rightMax[i+1])

        # loop lists to calcurate and added the amount of trapped water at each position

        for i in range(len(height)):
            total += min(leftMax[i], rightMax[i]) - height[i]

        return total
        
        


