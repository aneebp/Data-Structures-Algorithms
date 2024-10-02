class Solution:
    def rotate(self,nums,k):
        n = len(nums)
        #handles the case where k (the number of rotations) is larger than the length of the array
        k = k % n 
        #nums[:] modifies the original nums array in-place
        nums[:] = nums[-k:] + nums[:-k]
        print(nums)        

nums = [1,2,3,4,5,6,7]
k = 3
S1 = Solution()
result = S1.rotate(nums,k)
print(result)
