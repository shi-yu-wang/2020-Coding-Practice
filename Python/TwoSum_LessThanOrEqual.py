# Find the numbers of pairs whose sum is less than or equal to target

class Solution:
    """
    @param nums: an array of integer
    @param target: an integer
    @return: an integer
    """
    def twoSum5(self, nums, target):
        # write your code here
        if not nums:
            return 0
        
        n = len(nums)
        if n == 1:
            return 0
        
        nums.sort()
        
        left, right = 0, n - 1
        count = 0
        while left < right:
            if nums[left] + nums[right] > target:
                right -= 1
            else:
                count += right - left
                left += 1

        return count
            
