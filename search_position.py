nums = [1,3,5,6]
target = 6

class Solution:
    def searchInsert(self,nums,target):
        for i,value in enumerate(nums):
            if value == target:
                print(i)
           

S1 = Solution()
S1.searchInsert(nums=nums,target=target)