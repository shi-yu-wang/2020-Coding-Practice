class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        
        permutations = []
        self.dfs(nums, set(), [], permutations)
        return permutations
    
    def dfs(self, nums, visited, permutation, permutations):
        if len(nums) == len(permutation):
            permutations.append(list(permutation))
            return
        
        for num in nums:
            if num in visited:
                continue
            permutation.append(num)
            visited.add(num)
            self.dfs(nums, visited, permutation, permutations)
            visited.remove(num)
            permutation.pop()
            
