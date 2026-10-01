class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums = {}

        for i, n in enumerate(nums):
            if target - n in sums:
                return [sums[target - n], i]

            sums[n] = i