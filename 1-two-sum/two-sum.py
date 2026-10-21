class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = {}
        for i in range(len(nums)):
            tar = target - nums[i]
            if tar in check:
                return [i, check[tar]]
            check[nums[i]] = i

      