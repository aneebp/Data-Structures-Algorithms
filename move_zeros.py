nums = [0,1,0,3,12]

class Solution:
    def moveZeroes(self,nums):
        pointer_zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[pointer_zero] = nums[i]
                pointer_zero += 1
        for i in range(pointer_zero, len(nums)):
            nums[i] = 0
        
    
S1 = Solution()
result = S1.moveZeroes(nums)
print(nums)