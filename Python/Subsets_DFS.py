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
            results.append(subset)
            return 
        
        # Don't accept nums[index]
        self.dfs(nums, index + 1, subset, results)
        
        # Accept nums[index]
        subset = subset + [nums[index]]
        self.dfs(nums, index + 1, subset, results)
            
