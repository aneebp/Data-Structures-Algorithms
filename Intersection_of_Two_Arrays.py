class Solution(object):
    def intersection(self, nums1, nums2):
       num1 = set(nums1)
       num2 = set(nums2)
        #this will find the common value in two array
       result = num1.intersection(num2)

       return list(result)
        
nums1 = [1,2,2,1]
nums2 = [2,2,1]
S1 = Solution()
result = S1.intersection(nums1,nums2)
print(result)