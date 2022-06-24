class Solution(object):
    def productExceptSelf(self, nums):
        answer = [1 for _ in range(len(nums))]
        
        for i in range(len(nums)-1):
            answer[i+1] = answer[i] * nums[i]
        
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            answer[i] *= postfix
            postfix *= nums[i]
        
        return answer
    