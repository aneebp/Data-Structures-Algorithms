class Solution:
    def majorityElement(self,nums):
        nums.sort()
        n= len(nums)
        return nums[n//2]
    
nums = [3,2,3]
S1 = Solution()
result = S1.majorityElement(nums)
print(result)