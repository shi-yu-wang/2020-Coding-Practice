class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        
        permutations = []
        nums.sort()
        self.dfs(nums, [False] * len(nums), [], permutations)
        return permutations
    
    def dfs(self, nums, visited, permutation, permutations):
        if len(nums) == len(permutation):
            permutations.append(list(permutation))
            return
        
        for i in range(len(nums)):
            if visited[i]:
                continue
            
            if i > 0 and nums[i] == nums[i - 1] and visited[i - 1] == False:
                continue
                
            permutation.append(nums[i])
            visited[i] = True
            self.dfs(nums, visited, permutation, permutations)
            visited[i] = False
            permutation.pop()
