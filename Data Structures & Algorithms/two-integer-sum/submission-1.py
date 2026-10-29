class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dif = {}
        
        for i, num in enumerate(nums):
            if (target - num) in dif:
                return [dif[target - num], i]

            dif[num] = i