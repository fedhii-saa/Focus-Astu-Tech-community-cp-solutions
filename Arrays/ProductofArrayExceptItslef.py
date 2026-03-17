class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1]*n
        right = nums[-1]
        for i in range(1,n):
            answer[i] = answer[i-1]*nums[i-1]
        for i in range(n-2,-1,-1):
            answer[i] *= right
            right *= nums[i]
        return answer    
