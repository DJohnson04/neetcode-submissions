class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search_recursive(arr, target, low, high):
            if low > high:
                return -1
            
            mid = low + (high - low) // 2
            
            if mid >= len(arr):
                return -1

            if arr[mid] == target:
                return mid
            
            elif arr[mid] > target:
                return binary_search_recursive(arr, target, low, mid - 1)
            
            else:
                return binary_search_recursive(arr, target, mid + 1, high)
        return binary_search_recursive(nums, target, 0, len(nums)- 1)