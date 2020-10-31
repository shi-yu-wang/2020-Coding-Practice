class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []
        if not nums:
            return results
        
        nums.sort()
        self.dfs(nums, 0, [], results)
        return results
    
    def dfs(self, nums, index, subset, results):
        if index == len(nums):
        # We should new subset by [:]
            results.append(subset[:])
            return
        
        subset = subset + [nums[index]]
        self.dfs(nums, index + 1, subset, results)
        
        del subset[len(subset) - 1]
        self.dfs(nums, index + 1, subset, results)
