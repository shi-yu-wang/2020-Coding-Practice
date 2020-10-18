class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if not nums:
            return
        
        self.quickSort(nums, 0, len(nums) - 1)
        return nums
    
    def quickSort(self, A, start, end):
        if start >= end:
            return
        
        left = start
        right = end
        
        pivot = A[end]
        while left <= right:
            while left <= right and A[left] < pivot:
                left += 1
            while left <= right and A[right] > pivot:
                right -= 1
            
            if left <= right:
                temp = A[left]
                A[left] = A[right]
                A[right] = temp
                left += 1
                right -= 1
        
        self.quickSort(A, start, right)
        self.quickSort(A, left, end)
        
        
