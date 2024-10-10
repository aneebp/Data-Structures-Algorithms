class Solution:
    def searchInsert(self, nums, target):
        for i in range(len(nums)):
            if target == nums[i]:
                return i  # Return the index if found
            elif target < nums[i]:
                return i  # Return the index where the target should be inserted
        
        return len(nums)  # If target is greater than all elements, return the length of nums

nums = [1, 3, 5, 6]
target = 5
S1 = Solution()
result = S1.searchInsert(nums, target)
print(result)  # Output: 2
