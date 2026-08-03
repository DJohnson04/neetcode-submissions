class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_m = {}
        for el in nums:
            if el not in hash_m:
                hash_m[el] = 1
            else:
                return True
        return False