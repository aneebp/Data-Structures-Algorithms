nums1 =[1,2,3]
nums2 =[2,5,6]

class Solution:
    def merge(self,nums1,nums2):
       sorted_array = nums1 + nums2
       sorted_array.sort()
       return sorted_array


S1 = Solution()
result = S1.merge(nums1,nums2)
print(result)