class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Input: nums = [1,2,4,6] Output: [48,24,12,8]
        res = []
        n = len(nums)
        left = [1] * n
        right = [1] * n

        for i in range(1, n):
            left[i] = left[i-1] * nums[i-1]
        
        for i in range(n-2, -1, -1):
            right[i] = right[i+1] * nums[i+1]

        for i in range(n):
            res.append(right[i] * left[i])

        return res

