class NumArray:

    def __init__(self, nums: List[int]):
         self.prefix_sum = []
         total = 0
         for el in nums:
            total += el
            self.prefix_sum.append(total)
#-2, 0, 3, -5, 2, -1
# -2, -2, 1, -4, -2, -3
    def sumRange(self, left: int, right: int) -> int:
        if left <= 0:
            left_sum = 0
        else:
            left_sum = self.prefix_sum[left - 1]
        if right >= len(self.prefix_sum):
            right_sum = self.prefix_sum[-1]
        else:
            right_sum = self.prefix_sum[right]
        return right_sum - left_sum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)