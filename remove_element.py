nums= [3,2,2,3]
val = 3

class Solution:
    def removeElement(self,nums,val):
       index = 0
       for i in range(len(nums)):
           if nums[i] != val:
               nums[index] = nums[i]
               index += 1
       return index
    
    
    
Sl = Solution()
result =Sl.removeElement(nums,val)
print(nums[:result])
Sl.check(nums)

