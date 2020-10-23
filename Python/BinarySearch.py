class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binarySearch(nums, 0, len(nums) - 1, target)
    
    def binarySearch(self, nums, start, end, target):
        if start > end:
            return -1
        
        mid = (start + end) // 2
        
        if nums[mid] == target:
            return mid
        
        if nums[mid] < target:
            return self.binarySearch(nums, mid + 1, end, target)
        
        return self.binarySearch(nums, start, mid - 1, target)
