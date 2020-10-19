class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if not nums:
            return
        
        temp = [0] * len(nums)
        self.mergeSort(nums, 0, len(nums) - 1, temp)
        
        return nums
        
    def mergeSort(self, A, start, end, temp):
        if start >= end:
            return
        
        self.mergeSort(A, start, (start + end) // 2, temp)
        self.mergeSort(A, (start + end) // 2 + 1, end, temp)
        self.merge(A, start, end, temp)
        
    def merge(self, A, start, end, temp):
        middle = (start + end) // 2
        leftIndex = start
        rightIndex = middle + 1
        index = leftIndex
        
        while leftIndex <= middle and rightIndex <= end:
            if A[leftIndex] < A[rightIndex]:
                temp[index] = A[leftIndex]
                index += 1
                leftIndex += 1
            else:
                temp[index] = A[rightIndex]
                index += 1
                rightIndex += 1
        
        while leftIndex <= middle:
            temp[index] = A[leftIndex]
            index += 1
            leftIndex += 1
        while rightIndex <= end:
            temp[index] = A[rightIndex]
            index += 1
            rightIndex += 1

        for i in range(start, end + 1):
            A[i] = temp[i]
        
