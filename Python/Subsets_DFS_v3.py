class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []
        if not nums:
            return results
        
        nums.sort()
        self.dfs(nums, 0, [], results)
        return results
    
    def dfs(self, nums, startIndex, subset, results):
        results.append(subset[:])
        
        for i in range(startIndex, len(nums)):
            subset = subset + [nums[i]]
            self.dfs(nums, i + 1, subset, results)
            # Backtracking
            del subset[len(subset) - 1]
