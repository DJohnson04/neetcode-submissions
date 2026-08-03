class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_m = {}
        for index, el in enumerate(nums):
            if el in hash_m.keys() and el + el == target:
                return [min(index, hash_m[target-el]), max(index, hash_m[target-el])]

            hash_m[el] = index
            if target-el in hash_m.keys() and hash_m[el] != hash_m[target-el]:
                return [min(hash_m[el], hash_m[target-el]), max(hash_m[el], hash_m[target-el])]
        return []