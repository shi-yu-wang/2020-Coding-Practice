class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        results = []
        if not nums:
            return results
        
        nums.sort()
        self.subsetHelper(nums, 0, [], results)
        return results
    
    def subsetHelper(self, nums, startIndex, subset, results):
        results.append(subset[:])
        
        for i in range(startIndex, len(nums)):
            if i != 0 and nums[i] == nums[i - 1] and i > startIndex:
                continue
            
            subset = subset + [nums[i]]
            self.subsetHelper(nums, i + 1, subset, results)
            del subset[len(subset) - 1]
