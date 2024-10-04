class Solution(object):
    def canJump(self, nums):
        max_reachable = 0
        for i in range(len(nums)):
            if i > max_reachable:
                return False
            
            max_reachable = max(max_reachable, i + nums[i])
            print(max_reachable)
      
            if max_reachable >= len(nums) -1:
                return True
        return True
            




nums = [1,0,1,4]
S1 = Solution()
result = S1.canJump(nums)
print(result)