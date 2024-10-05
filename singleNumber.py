class Solution:
    def singleNumber(self, nums):
        result = 0
        for num in nums:
            result ^= num  # XOR operation
        return result

# Example usage:
nums = [2,2,1]
S1 = Solution()
result = S1.singleNumber(nums)
print(result)  # Output: 4
