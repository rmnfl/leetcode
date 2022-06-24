class Solution(object):
    def productExceptSelf(self, nums):
        prefix = [1 for _ in range(len(nums) + 1)]
        postfix = [1 for _ in range(len(nums) + 1)]
        answer = [1 for _ in range(len(nums))]
        
        for i in range(len(nums)):
            prefix[i+1] = prefix[i] * nums[i]
            
        for i in range(len(nums)-1, 0, -1):
            postfix[i-1] = postfix[i] * nums[i]
            
        for i in range(len(nums)):
            answer[i] = prefix[i]*postfix[i]
        
        return answer
    