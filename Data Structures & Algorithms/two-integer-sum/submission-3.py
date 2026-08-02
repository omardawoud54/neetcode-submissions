class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}
        for i, n in enumerate(nums):
            c = target - n
            if c in s:
                return [s[c], i]
            s[n] = i