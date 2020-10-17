class Solution:
    def twoSum(self, nums, target):
        if not nums:
            return [-1, -1]
        
        # nlogn
        numsidx = [
            (number, index)
            for index, number in enumerate(nums)
        ]
        
        numsidx.sort()
        
        # n
        left, right = 0, len(numsidx) - 1
        while left < right:
            if numsidx[left][0] + numsidx[right][0] > target:
                right -= 1
            elif numsidx[left][0] + numsidx[right][0] < target:
                left += 1
            else:
                return sorted([numsidx[left][1], numsidx[right][1]])
            
        return [-1, -1]
